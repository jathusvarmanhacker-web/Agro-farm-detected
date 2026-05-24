import { useState, useEffect, useRef, useCallback } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, AreaChart, Area } from "recharts";
import {
  Leaf, Droplets, Flame, Shield, CloudRain, Wind, Thermometer,
  Bot, Plus, Trash2, Bell, AlertTriangle, CheckCircle, Wifi,
  WifiOff, ChevronRight, Calendar, Sprout, Zap, Eye, Home,
  BarChart2, Lock, MessageSquare, Sun, Cloud
} from "lucide-react";
// ─── Main App ─────────────────────────────────────────────────────────────────
export default function AgroShieldAI() {      // ← THIS is the "main app"

  const [page, setPage] = useState("dashboard");
  const [sensors, setSensors] = useState({...});
  const [crops, setCrops] = useState([...]);
  const [city, setCity] = useState("Kandy");  // ← city state lives HERE
  const [time, setTime] = useState(...);

  // ... rest of the app
}

const FONTS = `
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@400;500;700&family=Instrument+Serif:ital@0;1&display=swap');
`;

const styles = `
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: #050e07; }

  :root {
    --bg: #050e07;
    --bg2: #0a160c;
    --bg3: #0f2014;
    --card: #091510;
    --border: #1a3320;
    --border2: #254535;
    --green: #3dff7a;
    --green2: #22c55e;
    --green3: #16a34a;
    --green-dim: rgba(61,255,122,0.08);
    --amber: #fbbf24;
    --red: #f87171;
    --blue: #60a5fa;
    --text: #e2f0e6;
    --text2: #7aaa88;
    --text3: #3d6648;
    --font-display: 'Syne', sans-serif;
    --font-body: 'Syne', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
  }

  .app { display: flex; height: 100vh; overflow: hidden; background: var(--bg); font-family: var(--font-body); color: var(--text); }

  /* Sidebar */
  .sidebar {
    width: 220px; min-width: 220px; background: var(--bg2);
    border-right: 1px solid var(--border);
    display: flex; flex-direction: column;
    padding: 0; overflow: hidden;
    position: relative;
  }
  .sidebar::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 200px;
    background: radial-gradient(ellipse at 50% 0%, rgba(61,255,122,0.07) 0%, transparent 70%);
    pointer-events: none;
  }
  .brand {
    padding: 22px 20px 16px;
    border-bottom: 1px solid var(--border);
  }
  .brand-icon {
    width: 36px; height: 36px; background: var(--green);
    border-radius: 10px; display: flex; align-items: center; justify-content: center;
    margin-bottom: 10px;
  }
  .brand-name {
    font-family: var(--font-display); font-weight: 800; font-size: 16px;
    color: var(--green); letter-spacing: -0.3px; line-height: 1;
  }
  .brand-sub { font-size: 10px; color: var(--text3); font-family: var(--font-mono); margin-top: 2px; letter-spacing: 1px; text-transform: uppercase; }

  .nav { flex: 1; padding: 12px 10px; display: flex; flex-direction: column; gap: 2px; }
  .nav-item {
    display: flex; align-items: center; gap: 10px;
    padding: 9px 12px; border-radius: 8px;
    cursor: pointer; transition: all 0.15s;
    font-size: 13px; font-weight: 600; color: var(--text3);
    border: 1px solid transparent;
    position: relative;
  }
  .nav-item:hover { background: var(--green-dim); color: var(--text2); }
  .nav-item.active {
    background: var(--green-dim); color: var(--green);
    border-color: rgba(61,255,122,0.15);
  }
  .nav-item.active::before {
    content: ''; position: absolute; left: 0; top: 50%; transform: translateY(-50%);
    width: 3px; height: 18px; background: var(--green); border-radius: 0 3px 3px 0;
  }
  .nav-badge {
    margin-left: auto; background: var(--red);
    color: white; font-size: 9px; font-family: var(--font-mono);
    padding: 1px 5px; border-radius: 99px; font-weight: 700;
  }
  .nav-badge.green { background: var(--green3); }

  .sidebar-status {
    padding: 12px 14px; border-top: 1px solid var(--border);
    display: flex; align-items: center; gap: 8px;
  }
  .status-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--green); animation: pulse 2s infinite; }
  @keyframes pulse { 0%,100%{opacity:1;box-shadow:0 0 0 0 rgba(61,255,122,0.4)} 50%{opacity:0.8;box-shadow:0 0 0 4px transparent} }
  .status-text { font-size: 10px; color: var(--text3); font-family: var(--font-mono); }

  /* Main */
  .main { flex: 1; display: flex; flex-direction: column; overflow: hidden; }

  .topbar {
    padding: 14px 24px; border-bottom: 1px solid var(--border);
    display: flex; align-items: center; justify-content: space-between;
    background: var(--bg2);
  }
  .page-title { font-family: var(--font-display); font-size: 20px; font-weight: 800; color: var(--text); }
  .page-sub { font-size: 11px; color: var(--text3); font-family: var(--font-mono); margin-top: 1px; }
  .topbar-right { display: flex; align-items: center; gap: 10px; }
  .arduino-badge {
    display: flex; align-items: center; gap: 6px;
    padding: 5px 10px; border-radius: 6px;
    font-size: 10px; font-family: var(--font-mono); font-weight: 700;
    letter-spacing: 0.5px;
  }
  .arduino-badge.connected { background: rgba(61,255,122,0.1); color: var(--green); border: 1px solid rgba(61,255,122,0.2); }
  .arduino-badge.disconnected { background: rgba(248,113,113,0.1); color: var(--red); border: 1px solid rgba(248,113,113,0.2); }
  .time-badge {
    padding: 5px 10px; border-radius: 6px; border: 1px solid var(--border2);
    font-size: 11px; font-family: var(--font-mono); color: var(--text2);
  }

  .content { flex: 1; overflow-y: auto; padding: 20px 24px; }
  .content::-webkit-scrollbar { width: 4px; }
  .content::-webkit-scrollbar-track { background: transparent; }
  .content::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 2px; }

  /* Cards */
  .grid { display: grid; gap: 14px; }
  .grid-4 { grid-template-columns: repeat(4, 1fr); }
  .grid-3 { grid-template-columns: repeat(3, 1fr); }
  .grid-2 { grid-template-columns: repeat(2, 1fr); }
  .grid-12 { grid-template-columns: 1fr 2fr; }

  .card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: 12px; padding: 16px;
    position: relative; overflow: hidden;
    transition: border-color 0.2s;
  }
  .card:hover { border-color: var(--border2); }
  .card-glow::after {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, var(--green), transparent);
    opacity: 0.4;
  }
  .card-glow-red::after { background: linear-gradient(90deg, transparent, var(--red), transparent); opacity: 0.6; }
  .card-glow-amber::after { background: linear-gradient(90deg, transparent, var(--amber), transparent); opacity: 0.6; }

  .sensor-card { display: flex; flex-direction: column; gap: 10px; }
  .sensor-top { display: flex; align-items: flex-start; justify-content: space-between; }
  .sensor-icon {
    width: 36px; height: 36px; border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    border: 1px solid;
  }
  .sensor-icon.green { background: rgba(61,255,122,0.1); border-color: rgba(61,255,122,0.2); color: var(--green); }
  .sensor-icon.blue { background: rgba(96,165,250,0.1); border-color: rgba(96,165,250,0.2); color: var(--blue); }
  .sensor-icon.red { background: rgba(248,113,113,0.1); border-color: rgba(248,113,113,0.2); color: var(--red); }
  .sensor-icon.amber { background: rgba(251,191,36,0.1); border-color: rgba(251,191,36,0.2); color: var(--amber); }

  .sensor-status { font-size: 9px; font-family: var(--font-mono); padding: 3px 7px; border-radius: 4px; font-weight: 700; letter-spacing: 0.8px; }
  .status-safe { background: rgba(61,255,122,0.12); color: var(--green); }
  .status-warn { background: rgba(251,191,36,0.12); color: var(--amber); }
  .status-danger { background: rgba(248,113,113,0.12); color: var(--red); animation: blink 1s infinite; }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.5} }
  .status-info { background: rgba(96,165,250,0.12); color: var(--blue); }

  .sensor-value { font-family: var(--font-mono); font-size: 28px; font-weight: 700; color: var(--text); line-height: 1; }
  .sensor-label { font-size: 11px; color: var(--text3); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }

  .progress-bar { height: 4px; background: var(--bg3); border-radius: 2px; overflow: hidden; }
  .progress-fill { height: 100%; border-radius: 2px; transition: width 1s ease; }
  .progress-green { background: linear-gradient(90deg, var(--green3), var(--green)); }
  .progress-blue { background: linear-gradient(90deg, #2563eb, var(--blue)); }
  .progress-red { background: linear-gradient(90deg, #dc2626, var(--red)); }
  .progress-amber { background: linear-gradient(90deg, #d97706, var(--amber)); }

  .section-title {
    font-family: var(--font-display); font-size: 13px; font-weight: 800;
    color: var(--text2); text-transform: uppercase; letter-spacing: 1px;
    margin-bottom: 12px; display: flex; align-items: center; gap: 8px;
  }
  .section-title::after { content: ''; flex: 1; height: 1px; background: var(--border); }

  /* Alert banner */
  .alert-banner {
    padding: 10px 14px; border-radius: 8px; margin-bottom: 14px;
    display: flex; align-items: center; gap: 10px; font-size: 12px; font-weight: 700;
    border: 1px solid;
    animation: slideIn 0.3s ease;
  }
  @keyframes slideIn { from{transform:translateY(-8px);opacity:0} to{transform:translateY(0);opacity:1} }
  .alert-fire { background: rgba(248,113,113,0.1); border-color: rgba(248,113,113,0.3); color: var(--red); }
  .alert-intruder { background: rgba(251,191,36,0.1); border-color: rgba(251,191,36,0.3); color: var(--amber); }
  .alert-rain { background: rgba(96,165,250,0.1); border-color: rgba(96,165,250,0.3); color: var(--blue); }

  /* Crops */
  .crop-card {
    background: var(--card); border: 1px solid var(--border); border-radius: 10px;
    padding: 14px; display: flex; gap: 12px; align-items: flex-start;
    transition: all 0.2s;
  }
  .crop-card:hover { border-color: var(--border2); transform: translateY(-1px); }
  .crop-emoji { font-size: 28px; line-height: 1; }
  .crop-info { flex: 1; }
  .crop-name { font-weight: 700; font-size: 14px; color: var(--text); }
  .crop-variety { font-size: 11px; color: var(--text3); font-family: var(--font-mono); }
  .crop-dates { display: flex; gap: 12px; margin-top: 8px; }
  .crop-date-item { display: flex; flex-direction: column; gap: 2px; }
  .crop-date-label { font-size: 9px; color: var(--text3); text-transform: uppercase; letter-spacing: 0.5px; font-family: var(--font-mono); }
  .crop-date-val { font-size: 11px; color: var(--text2); font-family: var(--font-mono); font-weight: 600; }
  .crop-harvest-badge {
    font-size: 9px; padding: 3px 8px; border-radius: 4px; font-family: var(--font-mono);
    font-weight: 700; white-space: nowrap; margin-top: 4px; display: inline-block;
  }
  .harvest-soon { background: rgba(251,191,36,0.15); color: var(--amber); border: 1px solid rgba(251,191,36,0.2); }
  .harvest-ok { background: rgba(61,255,122,0.1); color: var(--green2); border: 1px solid rgba(61,255,122,0.15); }
  .harvest-overdue { background: rgba(248,113,113,0.1); color: var(--red); border: 1px solid rgba(248,113,113,0.2); }
  .delete-btn {
    background: none; border: none; cursor: pointer; color: var(--text3);
    padding: 4px; border-radius: 4px; transition: color 0.15s;
  }
  .delete-btn:hover { color: var(--red); }

  /* Add crop form */
  .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 10px; }
  .form-group { display: flex; flex-direction: column; gap: 6px; }
  .form-label { font-size: 10px; color: var(--text3); font-family: var(--font-mono); text-transform: uppercase; letter-spacing: 0.5px; font-weight: 700; }
  .form-input {
    background: var(--bg3); border: 1px solid var(--border2); border-radius: 7px;
    padding: 8px 10px; font-size: 12px; color: var(--text); font-family: var(--font-body);
    outline: none; transition: border-color 0.15s;
  }
  .form-input:focus { border-color: var(--green3); }
  .btn-primary {
    background: var(--green); color: #050e07; border: none; border-radius: 7px;
    padding: 9px 16px; font-size: 12px; font-weight: 800; cursor: pointer;
    font-family: var(--font-display); display: flex; align-items: center; gap: 6px;
    transition: all 0.15s; width: 100%;
  }
  .btn-primary:hover { background: #5dffaa; transform: translateY(-1px); }
  .btn-primary:active { transform: translateY(0); }

  /* Weather */
  .weather-big {
    display: flex; align-items: center; gap: 20px; padding: 4px 0 12px;
  }
  .weather-temp { font-family: var(--font-mono); font-size: 52px; font-weight: 700; line-height: 1; color: var(--text); }
  .weather-desc { font-family: 'Instrument Serif', serif; font-style: italic; font-size: 18px; color: var(--text2); }
  .weather-meta { display: flex; flex-direction: column; gap: 4px; }

  .weather-stat { display: flex; align-items: center; gap: 8px; font-size: 12px; color: var(--text2); }
  .weather-forecast { display: flex; gap: 10px; margin-top: 4px; }
  .forecast-day {
    flex: 1; background: var(--bg3); border-radius: 8px; padding: 10px 8px;
    text-align: center; border: 1px solid var(--border);
  }
  .forecast-day-name { font-size: 9px; color: var(--text3); font-family: var(--font-mono); text-transform: uppercase; letter-spacing: 0.5px; }
  .forecast-icon { font-size: 20px; margin: 6px 0; }
  .forecast-temp { font-size: 13px; font-family: var(--font-mono); font-weight: 700; color: var(--text); }
  .forecast-rain { font-size: 9px; color: var(--blue); font-family: var(--font-mono); margin-top: 2px; }

  /* AI Chat */
  .chat-container { display: flex; flex-direction: column; height: calc(100vh - 140px); }
  .chat-messages {
    flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 12px;
    padding-bottom: 12px;
  }
  .chat-messages::-webkit-scrollbar { width: 3px; }
  .chat-messages::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 2px; }
  .chat-bubble {
    max-width: 80%; padding: 10px 14px; border-radius: 10px; font-size: 13px; line-height: 1.6;
    animation: fadeUp 0.2s ease;
  }
  @keyframes fadeUp { from{transform:translateY(6px);opacity:0} to{transform:translateY(0);opacity:1} }
  .chat-bubble.user {
    align-self: flex-end; background: rgba(61,255,122,0.12);
    border: 1px solid rgba(61,255,122,0.2); color: var(--text);
    border-bottom-right-radius: 3px;
  }
  .chat-bubble.ai {
    align-self: flex-start; background: var(--bg3);
    border: 1px solid var(--border2); color: var(--text);
    border-bottom-left-radius: 3px;
  }
  .chat-bubble.typing { color: var(--text3); font-style: italic; font-size: 12px; }
  .chat-input-row { display: flex; gap: 8px; padding-top: 12px; border-top: 1px solid var(--border); }
  .chat-input {
    flex: 1; background: var(--bg3); border: 1px solid var(--border2); border-radius: 8px;
    padding: 10px 14px; font-size: 13px; color: var(--text); font-family: var(--font-body);
    outline: none; resize: none; transition: border-color 0.15s;
  }
  .chat-input:focus { border-color: var(--green3); }
  .send-btn {
    background: var(--green); color: #050e07; border: none; border-radius: 8px;
    padding: 0 16px; cursor: pointer; font-weight: 800; font-family: var(--font-display);
    transition: all 0.15s; font-size: 13px;
  }
  .send-btn:hover { background: #5dffaa; }
  .send-btn:disabled { opacity: 0.4; cursor: not-allowed; }
  .lang-selector { display: flex; gap: 6px; margin-bottom: 10px; }
  .lang-btn {
    padding: 4px 10px; border-radius: 5px; font-size: 10px; font-family: var(--font-mono);
    cursor: pointer; border: 1px solid var(--border2); background: var(--bg3); color: var(--text3);
    font-weight: 700; transition: all 0.15s;
  }
  .lang-btn.active { background: rgba(61,255,122,0.12); color: var(--green); border-color: rgba(61,255,122,0.2); }

  /* Security */
  .security-big {
    text-align: center; padding: 20px 0;
  }
  .security-icon-big {
    width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center;
    justify-content: center; margin: 0 auto 12px; border: 2px solid;
    transition: all 0.3s;
  }
  .security-icon-big.secure { background: rgba(61,255,122,0.08); border-color: rgba(61,255,122,0.3); color: var(--green); }
  .security-icon-big.breach { background: rgba(248,113,113,0.1); border-color: rgba(248,113,113,0.4); color: var(--red); animation: shake 0.5s infinite; }
  @keyframes shake { 0%,100%{transform:translateX(0)} 25%{transform:translateX(-4px)} 75%{transform:translateX(4px)} }
  .security-status-text { font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; letter-spacing: 2px; }
  .log-item {
    display: flex; align-items: center; gap: 10px; padding: 8px 0;
    border-bottom: 1px solid var(--border); font-size: 12px;
  }
  .log-item:last-child { border-bottom: none; }
  .log-time { font-family: var(--font-mono); font-size: 10px; color: var(--text3); min-width: 60px; }
  .log-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }

  /* Chart */
  .recharts-tooltip-wrapper .recharts-default-tooltip {
    background: var(--bg3) !important; border: 1px solid var(--border2) !important;
    border-radius: 6px !important;
  }

  /* Harvest reminder pill */
  .reminder-item {
    display: flex; align-items: center; gap: 10px; padding: 10px 12px;
    background: var(--bg3); border-radius: 8px; border-left: 3px solid;
    font-size: 12px;
  }
  .reminder-item.soon { border-color: var(--amber); }
  .reminder-item.overdue { border-color: var(--red); }
`;

const CROP_EMOJIS = {
  tomato: "🍅", carrot: "🥕", lettuce: "🥬", pepper: "🫑", cucumber: "🥒",
  eggplant: "🍆", potato: "🥔", onion: "🧅", garlic: "🧄", spinach: "🌿",
  default: "🌱"
};

const getCropEmoji = (name) => {
  const lower = name.toLowerCase();
  for (const [key, emoji] of Object.entries(CROP_EMOJIS)) {
    if (lower.includes(key)) return emoji;
  }
  return CROP_EMOJIS.default;
};

const getDaysUntilHarvest = (harvestDate) => {
  const today = new Date();
  const harvest = new Date(harvestDate);
  const diff = Math.ceil((harvest - today) / (1000 * 60 * 60 * 24));
  return diff;
};

const MOCK_WEATHER = {
  temp: 28, humidity: 72, wind: 14, desc: "Partly cloudy",
  icon: "⛅",
  forecast: [
    { day: "Today", icon: "⛅", temp: 28, rain: "10%" },
    { day: "Mon", icon: "🌧", temp: 24, rain: "80%" },
    { day: "Tue", icon: "🌧", temp: 22, rain: "70%" },
    { day: "Wed", icon: "🌤", temp: 26, rain: "20%" },
    { day: "Thu", icon: "☀️", temp: 30, rain: "5%" },
    { day: "Fri", icon: "☀️", temp: 31, rain: "5%" },
    { day: "Sat", icon: "⛅", temp: 27, rain: "30%" },
  ]
};

function generateSoilHistory() {
  const now = Date.now();
  return Array.from({ length: 20 }, (_, i) => ({
    time: new Date(now - (19 - i) * 3000).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
    value: Math.floor(38 + Math.random() * 25)
  }));
}

// ─── Dashboard Page ──────────────────────────────────────────────────────────
function Dashboard({ sensors, alerts }) {
  const [history, setHistory] = useState(generateSoilHistory);

  useEffect(() => {
    const id = setInterval(() => {
      setHistory(prev => {
        const next = [...prev.slice(1), {
          time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
          value: Math.floor(38 + Math.random() * 25)
        }];
        return next;
      });
    }, 3000);
    return () => clearInterval(id);
  }, []);

  return (
    <div>
      {sensors.flame && (
        <div className="alert-banner alert-fire">
          <Flame size={16} /> 🚨 FIRE DETECTED — Check your garden immediately!
        </div>
      )}
      {sensors.intruder && (
        <div className="alert-banner alert-intruder">
          <AlertTriangle size={16} /> ⚠️ INTRUDER DETECTED in storage area!
        </div>
      )}
      {MOCK_WEATHER.forecast[1].rain === "80%" && (
        <div className="alert-banner alert-rain">
          <CloudRain size={16} /> 🌧 Rain expected tomorrow — Skip watering today
        </div>
      )}

      <p className="section-title">Live Sensor Data</p>
      <div className="grid grid-4" style={{ marginBottom: 16 }}>
        <div className={`card card-glow sensor-card ${sensors.moisture < 30 ? "card-glow-amber" : ""}`}>
          <div className="sensor-top">
            <div className="sensor-icon green"><Droplets size={16} /></div>
            <span className={`sensor-status ${sensors.moisture < 30 ? "status-warn" : "status-safe"}`}>
              {sensors.moisture < 30 ? "LOW" : "OK"}
            </span>
          </div>
          <div>
            <div className="sensor-value">{sensors.moisture}<span style={{ fontSize: 16, color: "var(--text3)" }}>%</span></div>
            <div className="sensor-label">Soil Moisture</div>
          </div>
          <div className="progress-bar">
            <div className="progress-fill progress-green" style={{ width: `${sensors.moisture}%` }} />
          </div>
        </div>

        <div className={`card sensor-card ${sensors.waterLevel === "LOW" ? "card-glow-amber" : "card-glow"}`}>
          <div className="sensor-top">
            <div className="sensor-icon blue"><Droplets size={16} /></div>
            <span className={`sensor-status ${sensors.waterLevel === "LOW" ? "status-warn" : "status-safe"}`}>
              {sensors.waterLevel}
            </span>
          </div>
          <div>
            <div className="sensor-value">{sensors.waterLevel === "HIGH" ? "85" : sensors.waterLevel === "MED" ? "50" : "15"}<span style={{ fontSize: 16, color: "var(--text3)" }}>%</span></div>
            <div className="sensor-label">Water Tank</div>
          </div>
          <div className="progress-bar">
            <div className="progress-fill progress-blue" style={{ width: sensors.waterLevel === "HIGH" ? "85%" : sensors.waterLevel === "MED" ? "50%" : "15%" }} />
          </div>
        </div>

        <div className={`card sensor-card ${sensors.flame ? "card-glow-red" : "card-glow"}`}>
          <div className="sensor-top">
            <div className={`sensor-icon ${sensors.flame ? "red" : "green"}`}><Flame size={16} /></div>
            <span className={`sensor-status ${sensors.flame ? "status-danger" : "status-safe"}`}>
              {sensors.flame ? "FIRE!" : "SAFE"}
            </span>
          </div>
          <div>
            <div className="sensor-value" style={{ color: sensors.flame ? "var(--red)" : "var(--text)" }}>
              {sensors.flame ? "1" : "0"}
            </div>
            <div className="sensor-label">Fire Sensor</div>
          </div>
          <div className="progress-bar">
            <div className="progress-fill progress-red" style={{ width: sensors.flame ? "100%" : "2%" }} />
          </div>
        </div>

        <div className={`card sensor-card ${sensors.intruder ? "card-glow-amber" : "card-glow"}`}>
          <div className="sensor-top">
            <div className={`sensor-icon ${sensors.intruder ? "amber" : "green"}`}><Shield size={16} /></div>
            <span className={`sensor-status ${sensors.intruder ? "status-warn" : "status-safe"}`}>
              {sensors.intruder ? "BREACH" : "SECURE"}
            </span>
          </div>
          <div>
            <div className="sensor-value" style={{ color: sensors.intruder ? "var(--amber)" : "var(--text)" }}>
              {sensors.intruder ? "!" : "✓"}
            </div>
            <div className="sensor-label">Storage Security</div>
          </div>
          <div className="progress-bar">
            <div className="progress-fill progress-amber" style={{ width: sensors.intruder ? "100%" : "0%" }} />
          </div>
        </div>
      </div>

      <div className="grid grid-12">
        <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <div className="card">
            <div className="section-title" style={{ fontSize: 11, marginBottom: 10 }}>Weather</div>
            <div className="weather-big">
              <div style={{ fontSize: 40 }}>{MOCK_WEATHER.icon}</div>
              <div>
                <div className="weather-temp">{MOCK_WEATHER.temp}°</div>
                <div className="weather-desc">{MOCK_WEATHER.desc}</div>
              </div>
            </div>
            <div style={{ display: "flex", gap: 16 }}>
              <div className="weather-stat"><Droplets size={12} />{MOCK_WEATHER.humidity}% humidity</div>
              <div className="weather-stat"><Wind size={12} />{MOCK_WEATHER.wind} km/h</div>
            </div>
          </div>
        </div>

        <div className="card card-glow">
          <div className="section-title" style={{ fontSize: 11, marginBottom: 14 }}>Soil Moisture History</div>
          <ResponsiveContainer width="100%" height={160}>
            <AreaChart data={history} margin={{ top: 5, right: 5, left: -20, bottom: 0 }}>
              <defs>
                <linearGradient id="soilGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3dff7a" stopOpacity={0.25} />
                  <stop offset="95%" stopColor="#3dff7a" stopOpacity={0} />
                </linearGradient>
              </defs>
              <XAxis dataKey="time" tick={{ fill: "#3d6648", fontSize: 9 }} axisLine={false} tickLine={false} />
              <YAxis tick={{ fill: "#3d6648", fontSize: 9 }} axisLine={false} tickLine={false} domain={[0, 100]} />
              <Tooltip
                contentStyle={{ background: "#0f2014", border: "1px solid #254535", borderRadius: 6, fontSize: 11 }}
                labelStyle={{ color: "#7aaa88" }}
                itemStyle={{ color: "#3dff7a" }}
              />
              <Area type="monotone" dataKey="value" stroke="#3dff7a" strokeWidth={2} fill="url(#soilGrad)" dot={false} />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}

// ─── Crops Page ──────────────────────────────────────────────────────────────
function Crops({ crops, setCrops }) {
  const [form, setForm] = useState({ name: "", variety: "", plantDate: "", harvestDate: "" });
  const [showForm, setShowForm] = useState(false);

  const addCrop = () => {
    if (!form.name || !form.plantDate || !form.harvestDate) return;
    setCrops(prev => [...prev, { ...form, id: Date.now() }]);
    setForm({ name: "", variety: "", plantDate: "", harvestDate: "" });
    setShowForm(false);
  };

  const reminders = crops.filter(c => {
    const d = getDaysUntilHarvest(c.harvestDate);
    return d <= 7;
  });

  return (
    <div>
      {reminders.length > 0 && (
        <div style={{ marginBottom: 16 }}>
          <p className="section-title">Harvest Reminders</p>
          <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
            {reminders.map(c => {
              const d = getDaysUntilHarvest(c.harvestDate);
              return (
                <div key={c.id} className={`reminder-item ${d < 0 ? "overdue" : "soon"}`}>
                  <span>{getCropEmoji(c.name)}</span>
                  <span style={{ flex: 1 }}>
                    <strong>{c.name}</strong>
                    {d < 0 ? ` — Overdue by ${Math.abs(d)} days!` :
                      d === 0 ? " — Ready to harvest TODAY!" :
                        ` — Ready in ${d} day${d !== 1 ? "s" : ""}!`}
                  </span>
                  <Bell size={13} style={{ color: d < 0 ? "var(--red)" : "var(--amber)" }} />
                </div>
              );
            })}
          </div>
        </div>
      )}

      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 12 }}>
        <p className="section-title" style={{ margin: 0 }}>Crops ({crops.length})</p>
        <button className="btn-primary" style={{ width: "auto", padding: "6px 12px", fontSize: 11 }} onClick={() => setShowForm(!showForm)}>
          <Plus size={13} /> Add Crop
        </button>
      </div>

      {showForm && (
        <div className="card" style={{ marginBottom: 14, borderColor: "rgba(61,255,122,0.2)" }}>
          <div style={{ fontSize: 12, fontWeight: 700, color: "var(--green)", marginBottom: 10, fontFamily: "var(--font-mono)" }}>NEW CROP</div>
          <div className="form-row">
            <div className="form-group">
              <label className="form-label">Crop Name</label>
              <input className="form-input" placeholder="Tomato" value={form.name} onChange={e => setForm(p => ({ ...p, name: e.target.value }))} />
            </div>
            <div className="form-group">
              <label className="form-label">Variety</label>
              <input className="form-input" placeholder="Cherry" value={form.variety} onChange={e => setForm(p => ({ ...p, variety: e.target.value }))} />
            </div>
          </div>
          <div className="form-row">
            <div className="form-group">
              <label className="form-label">Plant Date</label>
              <input type="date" className="form-input" value={form.plantDate} onChange={e => setForm(p => ({ ...p, plantDate: e.target.value }))} />
            </div>
            <div className="form-group">
              <label className="form-label">Harvest Date</label>
              <input type="date" className="form-input" value={form.harvestDate} onChange={e => setForm(p => ({ ...p, harvestDate: e.target.value }))} />
            </div>
          </div>
          <button className="btn-primary" onClick={addCrop}><Plus size={14} /> Add Crop</button>
        </div>
      )}

      {crops.length === 0 ? (
        <div className="card" style={{ textAlign: "center", padding: 32, color: "var(--text3)" }}>
          <Sprout size={32} style={{ margin: "0 auto 10px", opacity: 0.4 }} />
          <div style={{ fontSize: 13, fontFamily: "var(--font-mono)" }}>No crops added yet</div>
          <div style={{ fontSize: 11, marginTop: 4 }}>Click "Add Crop" to get started</div>
        </div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
          {crops.map(crop => {
            const d = getDaysUntilHarvest(crop.harvestDate);
            return (
              <div key={crop.id} className="crop-card">
                <span className="crop-emoji">{getCropEmoji(crop.name)}</span>
                <div className="crop-info">
                  <div className="crop-name">{crop.name}</div>
                  {crop.variety && <div className="crop-variety">var. {crop.variety}</div>}
                  <div className="crop-dates">
                    <div className="crop-date-item">
                      <span className="crop-date-label">Planted</span>
                      <span className="crop-date-val">{crop.plantDate}</span>
                    </div>
                    <div className="crop-date-item">
                      <span className="crop-date-label">Harvest</span>
                      <span className="crop-date-val">{crop.harvestDate}</span>
                    </div>
                  </div>
                  <span className={`crop-harvest-badge ${d < 0 ? "harvest-overdue" : d <= 7 ? "harvest-soon" : "harvest-ok"}`}>
                    {d < 0 ? `${Math.abs(d)}d overdue` : d === 0 ? "Harvest today!" : `${d} days left`}
                  </span>
                </div>
                <button className="delete-btn" onClick={() => setCrops(p => p.filter(c => c.id !== crop.id))}>
                  <Trash2 size={14} />
                </button>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

// ─── Weather Page ─────────────────────────────────────────────────────────────
function Weather() {
  return (
    <div>
      <div className="card card-glow" style={{ marginBottom: 14 }}>
        <div className="section-title" style={{ fontSize: 11 }}>Current Conditions — Kandy, LK</div>
        <div className="weather-big">
          <div style={{ fontSize: 60 }}>{MOCK_WEATHER.icon}</div>
          <div className="weather-meta">
            <div className="weather-temp">{MOCK_WEATHER.temp}°C</div>
            <div className="weather-desc">{MOCK_WEATHER.desc}</div>
            <div style={{ display: "flex", gap: 16, marginTop: 8 }}>
              <div className="weather-stat"><Droplets size={12} />{MOCK_WEATHER.humidity}%</div>
              <div className="weather-stat"><Wind size={12} />{MOCK_WEATHER.wind} km/h</div>
              <div className="weather-stat"><Thermometer size={12} />Feels 30°C</div>
            </div>
          </div>
        </div>

        <div className="alert-banner alert-rain" style={{ marginTop: 8, marginBottom: 0 }}>
          <CloudRain size={14} />
          <span>Rain expected Monday & Tuesday — No watering needed for 2 days</span>
        </div>
      </div>

      <p className="section-title">7-Day Forecast</p>
      <div className="weather-forecast">
        {MOCK_WEATHER.forecast.map((d, i) => (
          <div key={i} className="forecast-day" style={i === 1 || i === 2 ? { borderColor: "rgba(96,165,250,0.3)", background: "rgba(96,165,250,0.05)" } : {}}>
            <div className="forecast-day-name">{d.day}</div>
            <div className="forecast-icon">{d.icon}</div>
            <div className="forecast-temp">{d.temp}°</div>
            <div className="forecast-rain">{d.rain}</div>
          </div>
        ))}
      </div>

      <div className="grid grid-3" style={{ marginTop: 14 }}>
        <div className="card">
          <div style={{ fontSize: 11, color: "var(--text3)", fontFamily: "var(--font-mono)", marginBottom: 8 }}>WATERING ADVICE</div>
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <Droplets size={20} style={{ color: "var(--blue)" }} />
            <span style={{ fontSize: 13, color: "var(--text2)" }}>Skip watering today & tomorrow</span>
          </div>
        </div>
        <div className="card">
          <div style={{ fontSize: 11, color: "var(--text3)", fontFamily: "var(--font-mono)", marginBottom: 8 }}>UV INDEX</div>
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <Sun size={20} style={{ color: "var(--amber)" }} />
            <span style={{ fontSize: 13, color: "var(--text2)" }}>High — 7.2 · Use shading</span>
          </div>
        </div>
        <div className="card">
          <div style={{ fontSize: 11, color: "var(--text3)", fontFamily: "var(--font-mono)", marginBottom: 8 }}>GROWING CONDITIONS</div>
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <Leaf size={20} style={{ color: "var(--green)" }} />
            <span style={{ fontSize: 13, color: "var(--text2)" }}>Good for leafy greens</span>
          </div>
        </div>
      </div>
    </div>
  );
}

// ─── Security Page ────────────────────────────────────────────────────────────
function Security({ sensors }) {
  const [log, setLog] = useState([
    { time: "12:30", msg: "System armed", color: "var(--green)" },
    { time: "11:45", msg: "Storage accessed — authorized", color: "var(--text3)" },
    { time: "09:12", msg: "All clear", color: "var(--green)" },
  ]);

  useEffect(() => {
    if (sensors.intruder) {
      const t = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
      setLog(prev => [{ time: t, msg: "INTRUSION DETECTED", color: "var(--red)" }, ...prev].slice(0, 10));
    }
  }, [sensors.intruder]);

  useEffect(() => {
    if (sensors.flame) {
      const t = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
      setLog(prev => [{ time: t, msg: "FIRE ALERT TRIGGERED", color: "var(--red)" }, ...prev].slice(0, 10));
    }
  }, [sensors.flame]);

  return (
    <div>
      <div className="grid grid-2" style={{ marginBottom: 14 }}>
        <div className="card card-glow" style={{ textAlign: "center" }}>
          <div style={{ fontSize: 11, color: "var(--text3)", fontFamily: "var(--font-mono)", marginBottom: 10 }}>STORAGE SECURITY</div>
          <div className={`security-icon-big ${sensors.intruder ? "breach" : "secure"}`} style={{ width: 72, height: 72, margin: "0 auto 10px" }}>
            {sensors.intruder ? <AlertTriangle size={32} /> : <Shield size={32} />}
          </div>
          <div className={`security-status-text ${sensors.intruder ? "" : ""}`} style={{ color: sensors.intruder ? "var(--red)" : "var(--green)" }}>
            {sensors.intruder ? "INTRUDER DETECTED" : "ALL SECURE"}
          </div>
          <div style={{ fontSize: 11, color: "var(--text3)", marginTop: 6 }}>Ultrasonic sensor active</div>
        </div>

        <div className="card card-glow" style={{ textAlign: "center" }}>
          <div style={{ fontSize: 11, color: "var(--text3)", fontFamily: "var(--font-mono)", marginBottom: 10 }}>FIRE DETECTION</div>
          <div className={`security-icon-big ${sensors.flame ? "breach" : "secure"}`} style={{ width: 72, height: 72, margin: "0 auto 10px" }}>
            <Flame size={32} />
          </div>
          <div className="security-status-text" style={{ color: sensors.flame ? "var(--red)" : "var(--green)" }}>
            {sensors.flame ? "FIRE DETECTED" : "NO FIRE"}
          </div>
          <div style={{ fontSize: 11, color: "var(--text3)", marginTop: 6 }}>Flame sensor active</div>
        </div>
      </div>

      <p className="section-title">Security Log</p>
      <div className="card">
        {log.length === 0 ? (
          <div style={{ textAlign: "center", color: "var(--text3)", fontSize: 12, padding: 20 }}>No events recorded</div>
        ) : (
          log.map((l, i) => (
            <div key={i} className="log-item">
              <span className="log-time">{l.time}</span>
              <div className="log-dot" style={{ background: l.color }} />
              <span style={{ fontSize: 12, color: "var(--text2)" }}>{l.msg}</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

// ─── AI Chat Page ─────────────────────────────────────────────────────────────
function AIChat({ sensors }) {
  const [messages, setMessages] = useState([
    { role: "ai", text: "Hello! I'm AgroShield AI. Ask me anything about your garden — plant care, disease diagnosis, harvest timing, or storage tips. I can help in English, Tamil (தமிழ்), or Sinhala (සිංහල)!" }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [lang, setLang] = useState("English");
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;
    const userText = input.trim();
    setInput("");
    setMessages(prev => [...prev, { role: "user", text: userText }]);
    setLoading(true);

    const sensorContext = `Current garden sensor readings: Soil Moisture: ${sensors.moisture}%, Water Tank: ${sensors.waterLevel}, Fire Status: ${sensors.flame ? "FIRE DETECTED" : "Safe"}, Storage: ${sensors.intruder ? "INTRUDER DETECTED" : "Secure"}.`;
    const langInstruction = lang !== "English" ? `Please respond in ${lang}.` : "";

    try {
      const resp = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 1000,
          system: `You are AgroShield AI, an expert smart gardening and agricultural assistant integrated into a dashboard connected to Arduino sensors. You help farmers and gardeners with plant care, disease diagnosis, pest control, harvest timing, soil management, and storage protection. ${sensorContext} Be concise, practical, and helpful. ${langInstruction}`,
          messages: [{ role: "user", content: userText }]
        })
      });
      const data = await resp.json();
      const text = data.content?.map(b => b.text || "").join("") || "Sorry, I couldn't get a response.";
      setMessages(prev => [...prev, { role: "ai", text }]);
    } catch {
      setMessages(prev => [...prev, { role: "ai", text: "Connection error. Please check your network." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 10 }}>
        <div className="lang-selector">
          {["English", "தமிழ்", "සිංහල"].map(l => (
            <button key={l} className={`lang-btn ${lang === l ? "active" : ""}`} onClick={() => setLang(l)}>{l}</button>
          ))}
        </div>
        <div style={{ fontSize: 10, color: "var(--text3)", fontFamily: "var(--font-mono)" }}>POWERED BY CLAUDE AI</div>
      </div>

      <div className="chat-messages">
        {messages.map((m, i) => (
          <div key={i} className={`chat-bubble ${m.role}`} style={{ whiteSpace: "pre-wrap" }}>{m.text}</div>
        ))}
        {loading && <div className="chat-bubble ai typing">AgroShield AI is thinking...</div>}
        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-row">
        <textarea
          className="chat-input"
          rows={2}
          placeholder={lang === "தமிழ்" ? "உங்கள் கேள்வி தட்டச்சு செய்யவும்..." : lang === "සිංහල" ? "ඔබගේ ප්‍රශ්නය ටයිප් කරන්න..." : "Ask about plant care, diseases, harvest timing..."}
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); sendMessage(); } }}
        />
        <button className="send-btn" onClick={sendMessage} disabled={loading || !input.trim()}>
          Send
        </button>
      </div>
    </div>
  );
}

// ─── Main App ─────────────────────────────────────────────────────────────────
export default function AgroShieldAI() {
  const [page, setPage] = useState("dashboard");
  const [sensors, setSensors] = useState({
    moisture: 45,
    waterLevel: "MED",
    flame: false,
    intruder: false,
  });
  const [crops, setCrops] = useState([
    { id: 1, name: "Tomato", variety: "Thilina", plantDate: "2026-03-10", harvestDate: "2026-05-28" },
    { id: 2, name: "Carrot", variety: "Nantes", plantDate: "2026-04-01", harvestDate: "2026-07-01" },
    { id: 3, name: "Lettuce", variety: "Butter", plantDate: "2026-05-01", harvestDate: "2026-06-15" },
  ]);
  const [time, setTime] = useState(new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }));
  const [connected] = useState(true);

  // Simulate Arduino data
  useEffect(() => {
    const id = setInterval(() => {
      setSensors(prev => ({
        ...prev,
        moisture: Math.max(10, Math.min(90, prev.moisture + (Math.random() - 0.48) * 3)),
        waterLevel: prev.moisture < 25 ? "LOW" : prev.moisture < 60 ? "MED" : "HIGH",
      }));
      setTime(new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }));
    }, 3000);
    return () => clearInterval(id);
  }, []);

  const harvestAlerts = crops.filter(c => getDaysUntilHarvest(c.harvestDate) <= 3);
  const alerts = sensors.flame || sensors.intruder;

  const NAV = [
    { id: "dashboard", icon: <Home size={15} />, label: "Dashboard", badge: alerts ? "!" : null, badgeColor: "red" },
    { id: "crops", icon: <Sprout size={15} />, label: "Crops", badge: harvestAlerts.length || null, badgeColor: "green" },
    { id: "weather", icon: <CloudRain size={15} />, label: "Weather" },
    { id: "security", icon: <Shield size={15} />, label: "Security", badge: (sensors.flame || sensors.intruder) ? "!" : null, badgeColor: "red" },
    { id: "ai", icon: <Bot size={15} />, label: "AI Assistant" },
  ];

  const PAGE_TITLES = {
    dashboard: ["Dashboard", "Live sensor monitoring"],
    crops: ["Crop Manager", "Track & schedule harvests"],
    weather: ["Weather Intelligence", "Forecast & irrigation advice"],
    security: ["Security System", "Flame & intrusion monitoring"],
    ai: ["AI Assistant", "Smart farming help in 3 languages"],
  };

  return (
    <>
      <style>{FONTS + styles}</style>
      <div className="app">
        {/* Sidebar */}
        <div className="sidebar">
          <div className="brand">
            <div className="brand-icon"><Leaf size={20} color="#050e07" /></div>
            <div className="brand-name">AgroShield</div>
            <div className="brand-sub">AI Dashboard v1.0</div>
          </div>
          <nav className="nav">
            {NAV.map(n => (
              <div key={n.id} className={`nav-item ${page === n.id ? "active" : ""}`} onClick={() => setPage(n.id)}>
                {n.icon}
                {n.label}
                {n.badge && <span className={`nav-badge ${n.badgeColor || ""}`}>{n.badge}</span>}
              </div>
            ))}
          </nav>
          <div className="sidebar-status">
            <div className="status-dot" />
            <span className="status-text">ARDUINO {connected ? "CONNECTED" : "OFFLINE"}</span>
          </div>
        </div>

        {/* Main */}
        <div className="main">
          <div className="topbar">
            <div>
              <div className="page-title">{PAGE_TITLES[page][0]}</div>
              <div className="page-sub">{PAGE_TITLES[page][1]}</div>
            </div>
            <div className="topbar-right">
              <div className={`arduino-badge ${connected ? "connected" : "disconnected"}`}>
                {connected ? <Wifi size={11} /> : <WifiOff size={11} />}
                {connected ? "SERIAL ACTIVE" : "DISCONNECTED"}
              </div>
              <div className="time-badge">{time}</div>

              {/* Demo controls */}
              <div style={{ display: "flex", gap: 6 }}>
                <button
                  onClick={() => setSensors(p => ({ ...p, flame: !p.flame }))}
                  style={{
                    padding: "4px 8px", borderRadius: 5, fontSize: 9, cursor: "pointer",
                    fontFamily: "var(--font-mono)", fontWeight: 700,
                    background: sensors.flame ? "rgba(248,113,113,0.2)" : "var(--bg3)",
                    color: sensors.flame ? "var(--red)" : "var(--text3)",
                    border: `1px solid ${sensors.flame ? "rgba(248,113,113,0.3)" : "var(--border2)"}`,
                  }}
                >
                  🔥 FIRE SIM
                </button>
                <button
                  onClick={() => setSensors(p => ({ ...p, intruder: !p.intruder }))}
                  style={{
                    padding: "4px 8px", borderRadius: 5, fontSize: 9, cursor: "pointer",
                    fontFamily: "var(--font-mono)", fontWeight: 700,
                    background: sensors.intruder ? "rgba(251,191,36,0.15)" : "var(--bg3)",
                    color: sensors.intruder ? "var(--amber)" : "var(--text3)",
                    border: `1px solid ${sensors.intruder ? "rgba(251,191,36,0.3)" : "var(--border2)"}`,
                  }}
                >
                  👁 INTRUDE SIM
                </button>
              </div>
            </div>
          </div>

          <div className="content">
            {page === "dashboard" && <Dashboard sensors={sensors} />}
            {page === "crops" && <Crops crops={crops} setCrops={setCrops} />}
            {page === "weather" && <Weather />}
            {page === "security" && <Security sensors={sensors} />}
            {page === "ai" && <AIChat sensors={sensors} />}
          </div>
        </div>
      </div>
    </>
  );
}

