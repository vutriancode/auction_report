HOST  = "smtp.gmail.com"
USERNAME = "vutrian172933@gmail.com"
PASSWORD = "an.vt172933"
SUBJECT = " Thông báo diễn biến đấu giá trực tuyến"
JSON_TEST ={
    "Template": "LSTragia.docx",
    "ListData": {
        "nowday":15,
        "nowmonth":11,
        "nowyear":2021,
        "trung": True,
        "ReceiverCode":"KH0001",
        "RecieverName":"Công ty cổ phần Trường Sinh",
        "AssetOwner":"Công ty cổ phần Vũ Trí An",
        "Auctioneer":"Vũ Trí An",
        "DVDGTS":"Công ty đấu giá hợp danh Vũ Trí An",
        "history":[
            {
                "stt":1,
                "time":"2021-12-01T00:00:00.000",
                "assetcode":"TS0001",
                "customercode":"KH0001",
                "price":1000000,
                "note":""
            },
            {
                "stt":2,
                "time":"2021-12-01T00:00:00.000",
                "assetcode":"TS0001",
                "customercode":"KH0001",
                "price":2000000,
                "note":"Gía cao nhất"
            },
            {
                "stt":3,
                "time":"2021-12-01T00:00:00.000",
                "assetcode":"TS0002",
                "customercode":"KH0001",
                "price": 1000000,
                "note":"Gía cao nhất"
                }
            ]
        }
    }

HTML= '''\
<!doctype html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Simple Transactional Email</title>
    <style>
      /* -------------------------------------
          GLOBAL RESETS
      ------------------------------------- */
      
      /*All the styling goes here*/
      
      img {
        border: none;
        -ms-interpolation-mode: bicubic;
        max-width: 100%; 
      }

      body {
        background-color: #f6f6f6;
        font-family: sans-serif;
        -webkit-font-smoothing: antialiased;
        font-size: 14px;
        line-height: 1.4;
        margin: 0;
        padding: 0;
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%; 
      }

      table {
        border-collapse: separate;
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
        width: 100%; }
        table td {
          font-family: sans-serif;
          font-size: 14px;
          vertical-align: top; 
      }

      /* -------------------------------------
          BODY & CONTAINER
      ------------------------------------- */

      .body {
        background-color: #f6f6f6;
        width: 100%; 
      }

      /* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */
      .container {
        display: block;
        margin: 0 auto !important;
        /* makes it centered */
        max-width: 580px;
        padding: 10px;
        width: 580px; 
      }

      /* This should also be a block element, so that it will fill 100% of the .container */
      .content {
        box-sizing: border-box;
        display: block;
        margin: 0 auto;
        max-width: 580px;
        padding: 10px; 
      }

      /* -------------------------------------
          HEADER, FOOTER, MAIN
      ------------------------------------- */
      .main {
        background: #ffffff;
        border-radius: 3px;
        width: 100%; 
      }

      .wrapper {
        box-sizing: border-box;
        padding: 20px; 
      }

      .content-block {
        padding-bottom: 10px;
        padding-top: 10px;
      }

      .footer {
        clear: both;
        margin-top: 10px;
        text-align: center;
        width: 100%; 
      }
        .footer td,
        .footer p,
        .footer span,
        .footer a {
          color: #999999;
          font-size: 12px;
          text-align: center; 
      }

      /* -------------------------------------
          TYPOGRAPHY
      ------------------------------------- */
      h1,
      h2,
      h3,
      h4 {
        color: #000000;
        font-family: sans-serif;
        font-weight: 400;
        line-height: 1.4;
        margin: 0;
        margin-bottom: 30px; 
      }

      h1 {
        font-size: 35px;
        font-weight: 300;
        text-align: center;
        text-transform: capitalize; 
      }

      p,
      ul,
      ol {
        font-family: sans-serif;
        font-size: 14px;
        font-weight: normal;
        margin: 0;
        margin-bottom: 15px; 
      }
        p li,
        ul li,
        ol li {
          list-style-position: inside;
          margin-left: 5px; 
      }

      a {
        color: #3498db;
        text-decoration: underline; 
      }

      /* -------------------------------------
          BUTTONS
      ------------------------------------- */
      .btn {
        box-sizing: border-box;
        width: 100%; }
        .btn > tbody > tr > td {
          padding-bottom: 15px; }
        .btn table {
          width: auto; 
      }
        .btn table td {
          background-color: #ffffff;
          border-radius: 5px;
          text-align: center; 
      }
        .btn a {
          background-color: #ffffff;
          border: solid 1px #3498db;
          border-radius: 5px;
          box-sizing: border-box;
          color: #3498db;
          cursor: pointer;
          display: inline-block;
          font-size: 14px;
          font-weight: bold;
          margin: 0;
          padding: 12px 25px;
          text-decoration: none;
          text-transform: capitalize; 
      }

      .btn-primary table td {
        background-color: #3498db; 
      }

      .btn-primary a {
        background-color: #3498db;
        border-color: #3498db;
        color: #ffffff; 
      }

      /* -------------------------------------
          OTHER STYLES THAT MIGHT BE USEFUL
      ------------------------------------- */
      .last {
        margin-bottom: 0; 
      }

      .first {
        margin-top: 0; 
      }

      .align-center {
        text-align: center; 
      }

      .align-right {
        text-align: right; 
      }

      .align-left {
        text-align: left; 
      }

      .clear {
        clear: both; 
      }

      .mt0 {
        margin-top: 0; 
      }

      .mb0 {
        margin-bottom: 0; 
      }

      .preheader {
        color: transparent;
        display: none;
        height: 0;
        max-height: 0;
        max-width: 0;
        opacity: 0;
        overflow: hidden;
        mso-hide: all;
        visibility: hidden;
        width: 0; 
      }

      .powered-by a {
        text-decoration: none; 
      }

      hr {
        border: 0;
        border-bottom: 1px solid #f6f6f6;
        margin: 20px 0; 
      }

      /* -------------------------------------
          RESPONSIVE AND MOBILE FRIENDLY STYLES
      ------------------------------------- */
      @media only screen and (max-width: 620px) {
        table.body h1 {
          font-size: 28px !important;
          margin-bottom: 10px !important; 
        }
        table.body p,
        table.body ul,
        table.body ol,
        table.body td,
        table.body span,
        table.body a {
          font-size: 16px !important; 
        }
        table.body .wrapper,
        table.body .article {
          padding: 10px !important; 
        }
        table.body .content {
          padding: 0 !important; 
        }
        table.body .container {
          padding: 0 !important;
          width: 100% !important; 
        }
        table.body .main {
          border-left-width: 0 !important;
          border-radius: 0 !important;
          border-right-width: 0 !important; 
        }
        table.body .btn table {
          width: 100% !important; 
        }
        table.body .btn a {
          width: 100% !important; 
        }
        table.body .img-responsive {
          height: auto !important;
          max-width: 100% !important;
          width: auto !important; 
        }
      }

      /* -------------------------------------
          PRESERVE THESE STYLES IN THE HEAD
      ------------------------------------- */
      @media all {
        .ExternalClass {
          width: 100%; 
        }
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
          line-height: 100%; 
        }
        .apple-link a {
          color: inherit !important;
          font-family: inherit !important;
          font-size: inherit !important;
          font-weight: inherit !important;
          line-height: inherit !important;
          text-decoration: none !important; 
        }
        #MessageViewBody a {
          color: inherit;
          text-decoration: none;
          font-size: inherit;
          font-family: inherit;
          font-weight: inherit;
          line-height: inherit;
        }
        .btn-primary table td:hover {
          background-color: #34495e !important; 
        }
        .btn-primary a:hover {
          background-color: #34495e !important;
          border-color: #34495e !important; 
        } 
      }

    </style>
  </head>
  <body class="">
    <span class="preheader">Quý khách vừa tham gia phiên đấu giá trực tuyến do Đơn vị đấu giá - <strong>DVDGTS</strong> tổ chức </span>
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body">
      <tr>
        <td>&nbsp;</td>
        <td class="container">
          <div class="content">
            <div class="footer">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                  <tr>
                    <td class="content-block">
                        <img src="https://i.ibb.co/Qm8XQC7/logo.jpg" width="100" height="100">
                    </td>
                  </tr>
                </table>
              </div>

            <!-- START CENTERED WHITE CONTAINER -->
            <table role="presentation" class="main">

              <!-- START MAIN CONTENT AREA -->
              <tr>
                <td class="wrapper">
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                    <tr>
                      <td>
                        <p><strong>Kính gửi:  Khách hàng ReceiverCode</strong></p>
                        <p>Quý khách vừa tham gia phiên đấu giá trực tuyến do Đơn vị đấu giá - <strong>DVDGTS</strong> tổ chức <i>ngày nowday tháng nowmonth năm nowyear</i> bằng nền tảng kỹ thuật <strong>Đấu giá trực tuyến và trả giá điện tử theo thời gian thực</strong> được cung cấp bởi Công ty Cổ phần AutoDoc. Mọi diễn biến trả giá của Quý khách đã được lưu trữ, thống kê bằng thời gian thực. Quý khách vui lòng xem chi tiết tại file <strong>DIỄN BIẾN TRẢ GIÁ </strong>đính kèm.</p>
                        <p>Quý khách ĐĂNG KÝ tham gia khách hàng thường xuyên của  Sandaugia.net để nhận thêm nhiều thông tin đấu giá trên cả nước và nhiều ưu đãi khác tại từng thời điểm vui lòng xác thực tài khoản <a href="https://www.sandaugia.net/ReceiverCode}">tại đây</a></p>
                        <p>Quý khách là các tổ chức đấu giá chuyên nghiệp ĐĂNG KÝ tham gia mạng lưới đấu giá trực tuyến của <a href="https://www.sandaugia.net/DVDGTS">Sandaugia.net</a> để nhận nhiều tiện ích bổ trợ nghiệp vụ đấu giá tự động; hướng dẫn setup, chuyển giao công nghệ trang thiết bị phòng đấu giá trực tuyến tiêu chuẩn và nhiều ưu đãi khác tại từng thời điểm vui lòng xác thực tài khoản <a href="https://www.sandaugia.net/DVDGTS">tại đây</a></p>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>

            <!-- END MAIN CONTENT AREA -->
            </table>
            <!-- END CENTERED WHITE CONTAINER -->

            <!-- START FOOTER -->
            <div class="footer">
              <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td class="content-block">
                    <span class="apple-link">Sandaugia.net</span>
                    <br> TRUY CẬP <a href="http://sandaugia.net">TẠI ĐÂY</a>.
                  </td>
                </tr>
              </table>
            </div>
            <!-- END FOOTER -->

          </div>
        </td>
        <td>&nbsp;</td>
      </tr>
    </table>
  </body>
</html>
'''