// run.js
const { exec } = require('child_process');

// ִ�������� node ycx.js �������׼���
exec('node ycx.js', (error, stdout, stderr) => {
  if (error) {
    console.error(`Error executing ycx.js: ${error}`);
    return;
  }

  console.log('Output:', stdout);
});
