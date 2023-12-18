這裡使用COLAB去運行專案

基本上有的錯誤我應該都除錯了

**這是受測試的平台 : http://siliconexam.com/st-register.php**

+ COLAB第一版 https://colab.research.google.com/drive/1g3QVSRNPLAoJAYAsWHtVCqlvGY8yisU7?usp=sharing
+ COLAB第二版 https://colab.research.google.com/drive/125hhmR_kqsn4yB1pZgFz-i7UC8NyW-qA#scrollTo=IAthCUYNX_fN

此專案沒法百分百識別CAPTCHA，但嘗試訓練下來成功識別的機率其實挺高的

但其中其實有很多是一開始測試程式時驗證不出來的程式區塊(歲月的痕跡)

雖然有程式註解了，但我還是再來稍微解釋一下

原始網頁將不需要的文字區塊過濾，降低影響辨識的風險
![captcha](https://github.com/Trinity-SYT-SECURITY/Using-artificial-intelligence-to-crack-webpage-CAPTCHA/blob/main/program_verification/original-web-filter-string.png)


這是分析影像所關注的焦點，讓機器更容易識別出CAPTCHA的個別字元
![captcha](https://github.com/Trinity-SYT-SECURITY/Using-artificial-intelligence-to-crack-webpage-CAPTCHA/blob/main/program_verification/ROI.png)


這裡單獨抓出所有識別出的字元，主要就是驗證是否有成功識別
![captcha](https://github.com/Trinity-SYT-SECURITY/Using-artificial-intelligence-to-crack-webpage-CAPTCHA/blob/main/program_verification/Cut-and-identify-individual-captcha.png)

圖像二值化，二值化後的圖像只有黑跟白，使我們要的區塊在過濾雜訊後讓機器更容易識別出來
![captcha](https://github.com/Trinity-SYT-SECURITY/Using-artificial-intelligence-to-crack-webpage-CAPTCHA/blob/main/program_verification/successful-identification.png)


最後將識別出的驗證碼填入CAPTCHA驗證框中
![captcha](https://github.com/Trinity-SYT-SECURITY/Using-artificial-intelligence-to-crack-webpage-CAPTCHA/blob/main/program_verification/Fill-in-the-verification-box-after-identification.png)

![captcha](https://github.com/Trinity-SYT-SECURITY/Using-artificial-intelligence-to-crack-webpage-CAPTCHA/blob/main/program_verification/Validation-box-filled-successfully.png)

這裡在程式執行完後會產生的檔案，包含裁切的字元以及填入字串畫面
![captcha](https://github.com/Trinity-SYT-SECURITY/Using-artificial-intelligence-to-crack-webpage-CAPTCHA/blob/main/program_verification/The-file-you-should-run-out-of-after-training.png)

有任何問題請私訊我><
Email:sytyactfhaha@gmail.com
