<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Resume Matcher & Reviewer Pro</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.4.120/pdf.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #0f172a; color: #f8fafc; }
    </style>
</head>
<body class="min-h-screen p-4 md:p-8">

    <div class="max-w-5xl mx-auto">
        <header class="text-center mb-10">
            <h1 class="text-3xl md:text-5xl font-extrabold bg-gradient-to-r from-blue-400 to-teal-400 bg-clip-text text-transparent">
                Resume Reviewer AI Bot
            </h1>
            <p class="text-gray-400 mt-2 text-sm md:text-base">Instant ATS analysis, keyword optimization, and professional rewrite recommendations.</p>
        </header>

        <div class="bg-slate-800 rounded-2xl border border-slate-700 p-6 shadow-xl mb-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                
                <div>
                    <label class="block text-sm font-medium text-slate-300 mb-2">1. Upload Resume (PDF)</label>
                    <div class="border-2 border-dashed border-slate-600 rounded-lg p-8 text-center cursor-pointer hover:border-blue-500 transition relative h-[180px] flex flex-col justify-center items-center transition-all duration-200" id="dropzone">
                        <input type="file" id="resumeFile" accept=".pdf" class="absolute inset-0 w-full h-full opacity-0 cursor-pointer">
                        <div class="space-y-1 text-center" id="uploadPrompt">
                            <svg class="mx-auto h-12 w-12 text-slate-400" stroke="currentColor" fill="none" viewBox="0 0 48 48"><path d="M28 8H12a4 4 0 00-4 4v28a4 4 0 004 4h24a4 4 0 004-4V20L28 8z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M28 8v12h12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                            <p class="text-sm text-slate-300 font-medium">Drag & Drop Resume PDF Here</p>
                        </div>
                        <p id="fileName" class="text-sm text-teal-400 font-medium hidden text-center px-4"></p>
                    </div>
                </div>

                <div class="flex flex-col">
                    <label class="block text-sm font-medium text-slate-300 mb-2">2. Target Job Description</label>
                    <textarea id="jobDesc" placeholder="Paste the complete target job requirement details here..." class="w-full flex-grow bg-slate-900 border border-slate-700 rounded-lg p-3 text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 transition min-h-[180px] md:min-h-0"></textarea>
                </div>
            </div>

            <button id="analyzeBtn" class="w-full mt-6 bg-gradient-to-r from-blue-500 to-teal-500 text-white font-semibold py-3 px-6 rounded-lg shadow-lg hover:brightness-110 active:scale-[0.99] transition flex items-center justify-center space-x-2">
                <span>Analyze Optimization Score</span>
            </button>
        </div>

        <div id="loading" class="hidden text-center py-12">
            <div class="inline-block animate-spin rounded-full h-12 w-12 border-4 border-teal-500 border-t-transparent mb-4"></div>
            <p class="text-lg text-slate-300 font-medium animate-pulse">Extracting text & reviewing profile with Gemini AI...</p>
        </div>

        <div id="dashboard" class="hidden space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 flex flex-col items-center justify-center text-center shadow-xl">
                    <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-2">Match Rating Score</h3>
                    <div class="relative flex items-center justify-center">
                        <span id="scoreText" class="text-5xl md:text-6xl font-black text-teal-400">0%</span>
                    </div>
                </div>

                <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 md:col-span-2 shadow-xl">
                    <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-3">Identified Missing Target Keywords</h3>
                    <div id="keywordsList" class="flex flex-wrap gap-2"></div>
                </div>
            </div>

            <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-xl">
                <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-3">Formatting & Structural Fixes</h3>
                <p id="formattingFeedback" class="text-slate-300 leading-relaxed text-sm md:text-base whitespace-pre-line"></p>
            </div>

            <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-xl">
                <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-4">Recommended High-Impact Re-writes</h3>
                <div id="rewritesList" class="space-y-4"></div>
            </div>
        </div>
    </div>

    <script type="module">
        import { GoogleGenAI } from "https://esm.run/@google/genai";

        pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.4.120/pdf.worker.min.js';

        
        
        const EMBEDDED_API_KEY =""
        

        let extractedText = "";
        const dropzone = document.getElementById('dropzone');
        const fileInput = document.getElementById('resumeFile');

       
        async function processFile(file) {
            if (!file || file.type !== "application/pdf") {
                alert("Please upload a valid PDF file.");
                return;
            }
            
            document.getElementById('fileName').innerText = `✓ File loaded: ${file.name}`;
            document.getElementById('fileName').classList.remove('hidden');
            document.getElementById('uploadPrompt').classList.add('hidden');

            try {
                const reader = new FileReader();
                reader.onload = async function () {
                    const typedarray = new Uint8Array(this.result);
                    const pdf = await pdfjsLib.getDocument(typedarray).promise;
                    let text = "";
                    for (let i = 1; i <= pdf.numPages; i++) {
                        const page = await pdf.getPage(i);
                        const content = await page.getTextContent();
                        text += content.items.map(item => item.str).join(" ") + "\n";
                    }
                    extractedText = text.trim();
                };
                reader.readAsArrayBuffer(file);
            } catch (err) {
                alert("Error extracting text content from PDF.");
                console.error(err);
            }
        }

        
        fileInput.addEventListener('change', async (e) => {
            await processFile(e.target.files[0]);
        });

        
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropzone.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
            }, false);
        });

        ['dragenter', 'dragover'].forEach(eventName => {
            dropzone.addEventListener(eventName, () => {
                dropzone.classList.add('border-blue-500', 'bg-slate-700/50');
            }, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            dropzone.addEventListener(eventName, () => {
                dropzone.classList.remove('border-blue-500', 'bg-slate-700/50');
            }, false);
        });

        dropzone.addEventListener('drop', async (e) => {
            const dt = e.dataTransfer;
            const files = dt.files;
            if (files.length > 0) {
                fileInput.files = files; 
                await processFile(files[0]);
            }
        });

        
        document.getElementById('analyzeBtn').addEventListener('click', async () => {
            const jobDesc = document.getElementById('jobDesc').value.trim();

            if (!extractedText) return alert("Please drag & drop or click to upload a PDF Resume first.");
            if (!jobDesc) return alert("Please paste a target Job Description to compare against.");

            document.getElementById('dashboard').classList.add('hidden');
            document.getElementById('loading').classList.remove('hidden');

            try {
                const ai = new GoogleGenAI({ apiKey: EMBEDDED_API_KEY });
                
                const systemPrompt = `
                    You are an exceptionally strict, brutally honest, world-class Technical Recruiter and ATS (Applicant Tracking System) scanner. 
                    Your job is to critically evaluate the Resume Text directly against the targeted Job Description. Do not be polite. 
                    If a resume is bad, unprofessional, comical, or full of toxic red flags, give it the low score it deserves.

                    Look for these critical factors:
                    1. Context & Professionalism: Read the actual sentences. If the user mentions fireable offenses, bad attitudes, slang, or complete lack of professionalism, punish the score heavily. Do not let joke resumes pass with high match ratings simply because they keyword-stuffed technical names.
                    2. Keyword Alignment: Do they actually possess the skills in a functional configuration, or are they just spamming individual words?
                    3. Metrics: Deduct points if experience bullet points lack concrete, data-driven results (e.g., percentages, metrics, business impact metrics).
                    4.if the resume is same, give the same output as before you have given .dont change the output again and again

                    You must return your complete response in a valid, parsable JSON object format ONLY. Do not wrap code in markdown formatting backticks.
                    The JSON structure must exactly match this layout:
                    {
                        "match_score": 12,
                        "missing_keywords": ["Keyword1", "Keyword2"],
                        "formatting_feedback": "A string explicitly detailing the critical layout errors, professional gaps, or stylistic issues.",
                        "bullet_point_improvements": [
                            { "original": "text string", "improved": "text string" }
                        ]
                    }
                `;

                const response = await ai.models.generateContent({
                    model: 'gemini-2.5-flash',
                    contents: `Job Description:\n"${jobDesc}"\n\nResume Text:\n"${extractedText}"`,
                    config: {
                        systemInstruction: systemPrompt,
                        responseMimeType: "application/json"
                    }
                });

                let rawJson = response.text.trim();
                if (rawJson.startsWith("```json")) rawJson = rawJson.substring(7);
                if (rawJson.endsWith("```")) rawJson = rawJson.substring(0, rawJson.length - 3);

                const data = JSON.parse(rawJson.trim());

               
                document.getElementById('scoreText').innerText = `${data.match_score || 0}%`;
                
                
                if(data.match_score >= 80) document.getElementById('scoreText').className = "text-5xl md:text-6xl font-black text-emerald-400";
                else if(data.match_score >= 50) document.getElementById('scoreText').className = "text-5xl md:text-6xl font-black text-amber-400";
                else document.getElementById('scoreText').className = "text-5xl md:text-6xl font-black text-rose-500";

               
                const keywordsContainer = document.getElementById('keywordsList');
                keywordsContainer.innerHTML = '';
                if(data.missing_keywords && data.missing_keywords.length > 0) {
                    data.missing_keywords.forEach(kw => {
                        const span = document.createElement('span');
                        span.className = "bg-slate-900 border border-rose-500/30 text-rose-300 text-xs font-medium px-3 py-1.5 rounded-full shadow-inner";
                        span.innerText = kw;
                        keywordsContainer.appendChild(span);
                    });
                } else {
                    keywordsContainer.innerHTML = '<span class="text-emerald-400 text-sm font-medium">No missing keywords found! Look solid.</span>';
                }

                
                document.getElementById('formattingFeedback').innerText = data.formatting_feedback || "No systematic layout errors captured.";

                
                const rewritesContainer = document.getElementById('rewritesList');
                rewritesContainer.innerHTML = '';
                if(data.bullet_point_improvements && data.bullet_point_improvements.length > 0) {
                    data.bullet_point_improvements.forEach(item => {
                        const block = document.createElement('div');
                        block.className = "bg-slate-900 p-4 rounded-xl border border-slate-700/60 text-sm space-y-2 shadow-inner";
                        block.innerHTML = `
                            <p class="text-slate-400"><strong class="text-rose-400">Original List Point:</strong> ${item.original}</p>
                            <p class="text-slate-200"><strong class="text-emerald-400">Recommended Clean Rewrite:</strong> ${item.improved}</p>
                        `;
                        rewritesContainer.appendChild(block);
                    });
                } else {
                    rewritesContainer.innerHTML = '<p class="text-emerald-400 text-sm">Bullet structures are completely optimized with standard impact metrics.</p>';
                }

                
                document.getElementById('dashboard').classList.remove('hidden');

            } catch (error) {
                console.error(error);
                alert("AI Connection Error: Verify your API key is correct and valid.");
            } finally {
                document.getElementById('loading').classList.add('hidden');
            }
        });
    </script>
</body>
</html>
