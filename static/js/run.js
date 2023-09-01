// run.js
const { exec } = require('child_process');

// 执行命令行 node ycx.js 并捕获标准输出
exec('node ycx.js', (error, stdout, stderr) => {
  if (error) {
    console.error(`Error executing ycx.js: ${error}`);
    return;
  }

  console.log('Output:', stdout);
});
