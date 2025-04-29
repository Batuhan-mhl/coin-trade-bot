import threading
from keep_alive import keep_alive
from self_ping import self_ping
from telegram_utils import send_telegram_message
from coin_trade_bot_final_with_tp_sl import analyze_tp_sl
from macd_bollinger import analyze_macd_bollinger
from gainers_losers import report_gainers_losers
from sinyal_bot_gunluk import analyze_signals
from teknik_sinyal_bot import check_signals

def run_combined_bot():
    try:
        send_telegram_message("Bot başlatıldı, analizlere başlıyoruz!")
        analyze_signals()
        analyze_macd_bollinger()
        analyze_tp_sl()
        report_gainers_losers()
        check_signals()
    except Exception as e:
        send_telegram_message(f"Botta hata oluştu: {e}")

if __name__ == "__main__":
    keep_alive()
    send_telegram_message("Bot serverda başarıyla çalışıyor!")
    bot_thread = threading.Thread(target=run_combined_bot)
    bot_thread.start()
    ping_thread = threading.Thread(target=self_ping)
    ping_thread.start()
    
