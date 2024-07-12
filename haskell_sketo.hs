import System.IO
import Control.Monad
import Data.List
import System.Random
import Text.Printf
import Data.Time.Clock

-- Function for calculating the Euclidean distance from the point (0,0,0)
distanceFromOrigin :: Floating a => a -> a -> a -> a
distanceFromOrigin x y z = sqrt (x^2 + y^2 + z^2)

-- Comparison function for sorting tuples based on the first element (distance)
compareTuples :: Ord a => (a, b, c, d) -> (a, b, c, d) -> Ordering
compareTuples (a, _, _, _) (b, _, _, _) = compare a b

-- Implementation of the QUICKSORT algorithm
quicksort :: Ord a => [(a, b, c, d)] -> [(a, b, c, d)]
quicksort [] = []
quicksort (x:xs) = quicksort less ++ [x] ++ quicksort greater
  where
    less = filter (\y -> compareTuples y x == LT) xs
    greater = filter (\y -> compareTuples y x /= LT) xs

-- Function for reading data from the file, calculating distances, and sorting the points
readFileAndCalculateDistance :: FilePath -> IO [(Double, Double, Double, Double)]
readFileAndCalculateDistance fileName = do
    contents <- readFile fileName
    let points = map (\line -> let [x, y, z] = map read (words line)
                                   dist = distanceFromOrigin x y z
                               in (dist, x, y, z)) (lines contents)
    return $ quicksort points

-- List of file paths
filePaths :: [FilePath]
filePaths = ["input1000.txt", "input10000.txt", "input100000.txt", "input1000000.txt"]

-- Function to measure execution time
measureTime :: IO a -> IO NominalDiffTime
measureTime action = do
    startTime <- getCurrentTime
    _ <- action
    endTime <- getCurrentTime
    return (diffUTCTime endTime startTime)

-- Main function for processing each file and measuring execution time
main :: IO ()
main = do
    let iterations = 10
    forM_ filePaths $ \filePath -> do
        times <- replicateM iterations (measureTime $ readFileAndCalculateDistance filePath)
        let averageTime = sum times / fromIntegral iterations
        printf "Average execution time for %s: %.6f microseconds\n" filePath (realToFrac averageTime * 1000000 :: Double)