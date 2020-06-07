const chromium = require('chrome-aws-lambda');

module.exports.handler = async (event, context) => {
  let input;
  try {
    input = JSON.parse(event.body);
  } catch (e) {
    input = event.body;
  }
  let id = input.id;
  let pwd = input.password;

  const browser = await chromium.puppeteer.launch({
    executablePath: await chromium.executablePath,
    args: chromium.args,
    defaultViewport: chromium.defaultViewport,
    headless: chromium.headless,
    slowMo:250,
  });

  const page = await browser.newPage();

  let loginUrl = "https://signinssl.gmarket.co.kr/LogIn/LogIn?URL=http://myg.gmarket.co.kr/ContractList/ContractList"

  await page.goto(loginUrl);

  await page.evaluate((id, pwd) => {
    document.querySelector('#id').value = id;
    document.querySelector('#pwd').value = pwd;
  }, id, pwd);

  await page.$eval('.button_login', form => form.click());


  await browser.close();
  message = "test"
  return {
    statusCode: 200,
    body: JSON.stringify({
      message: ` Data is Here : ${message}`
    })
  }

}