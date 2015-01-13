## Rank Scores
SELECT Score,
       CASE
          WHEN @prevRank = Score THEN @curRank
          WHEN @prevRank := Score THEN @curRank := @curRank + 1
          WHEN @curRank := @curRank + 1 THEN @curRank
       END AS Rank
FROM Scores, (SELECT @curRank := 0, @prevRank := NULL) t
ORDER BY Score DESC
