import requests
import json

url = "http://localhost:3125/draft"

# TODO: Add an image. The image should be part of the data, base64 encode a jpg and use it with <img src="data:....." />
template = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
      <style>
     body {
margin-left:20px;
margin-right:20px;
     direction: rtl;
      text-align: right;
    }

    @media print {
      @page {
        size: A4;
      }

      body {
        margin-left:3cm;
margin-right:3cm;
      }

      header {
        position: fixed;
        top: 0;
        height: 3cm;
        border-bottom: 1px solid #000;
        background-color: white; /* Ensure the header has a background */
                z-index: 1000;

      }

      footer {
        position: fixed;
        bottom: 0;
        height: 3cm;
        text-align: center;
        border-top: 1px solid #000;
        background-color: white; /* Ensure the footer has a background */
        z-index: 1000;

      } introduction{
    color:red;
    }

      section {
        font-family: 'Segoe UI', sans-serif;
        margin-top: 4cm;  /* Space for the header */
        margin-bottom: 4cm;  /* Space for the footer */
        page-break-before: auto;
        page-break-after: auto;
        page-break-inside: avoid;


      }
 
    }

   table {
      width: 100%;
      border-collapse: collapse;
    }

    th, td {
      border: 1px solid #000;
      padding: 8px;
      text-align: center;
    }
    h1{
      color: #1A405D;
    }
    h2{
      font-weight: bold;
      color: #1A405D;
      font-size: 14pt;
    }
    h3{
      font-weight: bold;
      font-size: 12pt;
      color: #005DA0;
    }
    h4{
      font-size: 8pt;
      color: #005DA0;
      font-weight: bold;
    }
  </style>
</head>
<body>
    <header style="display: flex; justify-content: space-around;padding:0.5cm;">
      <img src="data:image/jpg;base64,{{ logo }}" alt="Authority Logo" style="width:2.2cm;height:0.8cm;margin-left:0.4cm;margin-top:0.3cm;"/>
      <div id="header_text">
      <p style="font-weight: bold; font-size: 8pt;">הדו"ח הנ"ל הינו ראשוני בלבד, תוכנו והמידע הכלול אינו מהווה מידע רשמי וסופי ואינו מחייב את רשות העתיקות עד לפרסום הדו"ח המדעי הסופי.</p>
      <p style="color:grey; font-size: 8pt;">© כל הזכויות שמורות לרשות העתיקות</p></div>
    </header>
  <div>
<section style="padding-top: 4cm; padding-bottom: 4cm;">
      <h2 style="color: #1A405D;">הקדמה</h2>
      <div style="font-size: 12pt;" > <p>
        רשות העתיקות אחראית על עתיקות הארץ ואתריה, במסגרת זו הרשות פועלת לשמור,
        לחשוף, לשמר, לחקור ולפרסם את עתיקות הארץ ואתריה בישראל ומחוצה לה. ברחבי
        מדינת ישראל קיימים כשלושים אלף אתרים המוגדרים כאתרי עתיקות. אתרים אלה
        וממצאיהם מהווים את מורשת התרבות החומרית של ארץ ישראל, ומשרטטים את קורותיה
        ואת תולדות האדם, העמים והממלכות שחיו כאן במהלך מאות ואלפי השנים האחרונות
      </p>
      <p>
        רשות העתיקות מעודדת את אזרחי המדינה לפעול למען השמירה על עתיקות הארץ
        ומניעת כל פגיעה בהם, כיוון שכל פגיעה כזו יש בה משום נזק בלתי הפיך למורשת
        העבר.
      </p>
      <p>
        חוק העתיקות )התשל"ח - 1978 ( וחוק רשות העתיקות )התשמ"ט - 1989 ( מטפלים בכל
        ענייני העתיקות של מדינת ישראל ביבשה ובים, ומכתיבים את הפעולות לשמירה על
        האיזון הראוי בין צרכי הפיתוח של הארץ לבין השמירה על עתיקותיה. במסגרת
        פעולות אלו ביצעה רשות העתיקות סקר. הדוח שלהלן מפרט את הפעולות
        הארכיאולוגיות שבוצעו בשטח במסגרת הפרויקט.
      </p>
      <p>
        בנוסף מצורף לדוח מסמך הנחיות ובו סיכום הפעולות לביצוע לצורך המשך הפיתוח.
      </p> <div>
  
        <div id="signature" style="font-size: 10pt;display:flex; flex-direction:column;">
        <span>בברכה,</span>
        <span>{{arch_name}}</span>
        <span>ארכיאולוג מרחב {{merchav}} </span>
      </div> 
  

    <div style="display: flex; justify-content: space-around;">
    <h3>מרחב: {{ merchav }}</h3>
    <h3>הרשאה: {{ license }}</h3>
    </div>
      
      <h1 style="text-align:center">{{ report_name }}</h1>
      <div style="display: flex; justify-content: flex-start;">    
      <h4 style="margin-left: 20px;">דוח ראשוני ליזם</h4>
      <h4>סוג ביצוע: {{ report_type }}</h4></div>
  
   <h2 >מבוא</h2>
      <p>{{introduction}}</p>
      <h2 {% if data.report_type !== 'excavation' %}
  >אופן הבדיקה</h2>
      <p>
        This is a paragraph that explains the method of archaeological checking.
      </p>
        <h2>רקע ארכיאולוגי</h2>
    <p>{{archeologic_background}}</p>
    <h2>תוצאות {{report_type_hebrew}}</h2>
    <p>{{HB_results}}</p>
    
      <h2>ממצאים</h2>
      <table>
        <thead>
          <tr>
            <th>מספר</th>
            <th>תאור</th>
            <th>אלמנט</th>
            <th>תקופה</th>
            <th>עומק</th>
            <th>X</th>
            <th>Y</th>
          </tr>
        </thead>
        <tbody>
    {{#each findings}}
          <tr>
             <td>{{this.number}}</td>
      <td>{{this.description}}</td>
      <td>{{this.element}}</td>
      <td>{{this.period}}</td>
      <td>{{this.depth}}</td>
      <td>{{this.x}}</td>
      <td>{{this.y}}</td>
          </tr>
    {{/each}}
        </tbody>
      </table>
  
    <div id="img">
      <img src="data:image/jpg;base64,{{ image }}" alt="Finding Image" />
    </div>
  
    <div id="recommendation" style="display: flex; justify-content: flex-start;">
      <h3 style="margin-left: 20px;">המלצה</h3>
      <h3>{{ recommendation }}</h3>
    </div>
  
    <div id="comments">
      <h2>הערות</h2>
      <p>{{ comments }}</p>
    </div>
  
    <div id="conclusion">
      <h2>סיומת דוח/ביבליוגרפיה</h2>
      <p>{{ conclusion }}</p>
    </div>
  
        <div id="signature" style="font-size: 10pt;display:flex; flex-direction:column;">
      <span>בברכה,</span>
      <span>{{ arch_name }}</span>
      <span>עורך הדו"ח</span>
    </div>
  </section>
    <footer>
    <p>זכויות היוצרים הם של רשות העתיקות. אין לשכפל, להעתיק, לצלם, להקליט, לתרגם,לאחסן במאגר מידע, לסדר או לקלוט בכל דרך ובכל אמצעי אלקטרוני, אופטי או מכני אחר - כל חלק שהוא מחומר זה ללא הסכמת רשות העתיקות</p>
      <p>© כל הזכויות שמורות לרשות העתיקות</p>
    </footer>
  </body>
</html>
"""
payload = json.dumps({
  "template": template,
  "data": {
  "title": "שלום עולם",
  "description": "זהו PDF שמציג טקסט בעברית",
  "items": [
            "פריט 1",
            "פריט 2",
            "פריט 3"
        ],
  "reshut_icon": "<base64 encoded image>", 
  "intro_text": "רשות העתיקות אחראית על עתיקות הארץ ואתריה ...",
  "merchav": "ירושלים",
  "license": "12345",
  "logo":"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",
  "report_name": "דוח חפירות",
  "report_type": "חתכי בדיקה",
  "findings": [
    {
      "number": 1,
      "description": "תיאור הממצא הראשון",
      "element": "אלמנט 1",
      "period": "תקופה 1",
      "depth": "1.5 מ'",
      "x": "30.123",
      "y": "35.678"
    },
    {
      "number": 2,
      "description": "תיאור הממצא השני",
      "element": "אלמנט 2",
      "period": "תקופה 2",
      "depth": "2.0 מ'",
      "x": "30.124",
      "y": "35.679"
    }
  ],
  "recommendation": "ההמלצה כאן",
  "comments": "הערות נוספות",
  "conclusion": "מסקנות הדו\"ח",
  "arch_name": "שדמן עמית",
  "role": "ארכאולוג מרחב"
      }
})

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
# Save the PDF file
if response.status_code != 200:
    print("Error!")
    print(response.text)
else:
  with open("output.pdf", "wb") as f:
      f.write(response.content)
  print("PDF file saved as output.pdf")
