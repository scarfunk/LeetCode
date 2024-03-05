/**
 * @param {number[][]} grid
 * @return {number}
 */
var uniquePathsIII = function(grid) {
  var x_len = grid.length
  var y_len = grid[0].length
  var need = grid.flat().filter(g=>g === 0).length + 1 // 처음 시작 1도 추가
  var result = 0;
  var dfs = function(x,y) {
    // 범위를 벗어나거나, 방문했으면 리턴.
    if(x < 0 || y < 0 || x >= x_len || y >= y_len || grid[x][y] < 0) return;
    // 목적지 need 가 0이면 찾은 것
    if(grid[x][y] === 2) {
      if(need === 0) {
        result++;
      }
    } else {
      grid[x][y] = -2; // 방문을 -2 로 기록
      need--;
      var x_dir = [1, -1, 0, 0];
      var y_dir = [0, 0, 1, -1];
      for(var i = 0; i < x_dir.length; i++) {
        var mx = x + x_dir[i];
        var my = y + y_dir[i];
        dfs(mx,my)
      }
      grid[x][y] = 0; // 방문기록을 초기화
      need++;
    }
  }
  // (1) 의 xy 를 찾는다.
  for(var i = 0; i < x_len; i++) {
    for(var j = 0; j < y_len; j++) {
      if(grid[i][j] === 1) {
        dfs(i,j)
      }
    }
  }
  return result;
};