import json
import os

day1_data = [
  {
    "question": "According to the speaker, why should beginners avoid Futures & Options (F&O) trading?",
    "options": [
      "It is illegal for retail investors.",
      "It requires huge capital, systemic knowledge, and is like gambling without them.",
      "It offers very low returns compared to mutual funds.",
      "It is restricted only to government employees."
    ],
    "answer": "It requires huge capital, systemic knowledge, and is like gambling without them.",
    "explanation": "🏗️ Khan: F&O is structurally designed for large-cap players and requires immense risk capital, discipline, and deep systemic knowledge. 🔥 Zara: It's basically a casino if you don't know what you're doing! Protect your stash and stay away until you're a market whale!"
  },
  {
    "question": "What is the core rule regarding the source of funds for investing in the stock market?",
    "options": [
      "Always take a personal loan to maximize your leverage.",
      "Borrow from friends only when the market is at an all-time low.",
      "Only invest money that you won't need for the next 3 to 4 years.",
      "Invest your daily living expenses to force yourself to make profits."
    ],
    "answer": "Only invest money that you won't need for the next 3 to 4 years.",
    "explanation": "🏗️ Khan: Borrowing capital introduces a fixed interest burden, undermining the compounding process when the market inevitably fluctuates. 🔥 Zara: Never invest with a ticking time bomb! Use your own spare cash so you can ride out the market dips without losing sleep!"
  },
  {
    "question": "Does a falling stock price automatically mean the company is fundamentally bad?",
    "options": [
      "Yes, price perfectly reflects the true underlying quality of the business.",
      "No, price movement is often driven by market sentiment rather than business fundamentals.",
      "Yes, a falling price means the company is going bankrupt.",
      "No, but it means the stock should be immediately sold to prevent total loss."
    ],
    "answer": "No, price movement is often driven by market sentiment rather than business fundamentals.",
    "explanation": "🏗️ Khan: A business's intrinsic value is derived from its financials and profitability, which often disconnects from short-term market sentiment. 🔥 Zara: Don't panic when the price drops! Sometimes the market is just catching a cold, while the company itself is still totally on fire!"
  },
  {
    "question": "How should a value investor apply the concept of a 'stop-loss' in equity investing?",
    "options": [
      "By automatically selling a stock if its price drops by 10%.",
      "By using technical trading software to trigger automated sales daily.",
      "By focusing on company selection, business quality, and financial evaluation rather than just price.",
      "By never selling a stock, even if the business fundamentals completely fail."
    ],
    "answer": "By focusing on company selection, business quality, and financial evaluation rather than just price.",
    "explanation": "🏗️ Khan: True risk management is established at the foundation: buying robust businesses. Price-based stop losses in equity often trigger premature exits. 🔥 Zara: A 20% drop isn't a red flag if the company is still crushing its sales! Use your brain for stop-loss, not a random price target!"
  },
  {
    "question": "What behavioral trap is triggered by checking your stock portfolio every single day?",
    "options": [
      "It increases your overall compounding rate and market awareness.",
      "It leads to emotional instability and compromises your trading discipline.",
      "It helps the stock price recover faster through active monitoring.",
      "It makes you completely immune to market volatility."
    ],
    "answer": "It leads to emotional instability and compromises your trading discipline.",
    "explanation": "🏗️ Khan: Frequent portfolio monitoring creates behavioral friction, overriding rational frameworks with short-term emotional reactions. 🔥 Zara: Stop obsessing over the red and green numbers every day! You're just torturing yourself and ruining the whole game plan!"
  },
  {
    "question": "Why is putting all your capital into a single stock considered a critical mistake?",
    "options": [
      "It guarantees a 100% return in one year but alerts the tax authorities.",
      "It prevents you from tracking the stock's price movements properly.",
      "It destroys emotional stability if the stock falls and ignores basic risk management.",
      "The stock market algorithm will automatically reject your trade."
    ],
    "answer": "It destroys emotional stability if the stock falls and ignores basic risk management.",
    "explanation": "🏗️ Khan: Heavy concentration mathematically amplifies risk without proportionately increasing the structural probability of success. Diversification is necessary. 🔥 Zara: Going all-in on one stock is a one-way ticket to Panic Town! Spread the love to protect your sanity!"
  },
  {
    "question": "According to the framework discussed, what defines a 'Right Decision' in the stock market?",
    "options": [
      "A decision that results in an immediate profit within one week.",
      "A decision made by following the advice of mainstream media and influencers.",
      "A decision that strictly follows the established process and framework, regardless of immediate price movement.",
      "A decision where the stock price never drops below your purchase price."
    ],
    "answer": "A decision that strictly follows the established process and framework, regardless of immediate price movement.",
    "explanation": "🏗️ Khan: Process orientation dictates that a statistically sound methodology defines correctness, not the immediate short-term outcome. 🔥 Zara: As long as you stuck to the rules and did your homework, you nailed it—even if the market throws a temporary tantrum!"
  },
  {
    "question": "What does the 'Tomato in a fruit salad' analogy illustrate about stock market success?",
    "options": [
      "Knowing theoretical concepts (intelligence) is useless without the practical execution and emotional control (wisdom) to make money.",
      "You should solely invest in agricultural and food-based stocks.",
      "Theoretical knowledge from universities automatically guarantees high market returns.",
      "Experienced truck drivers always make the best stock market investors."
    ],
    "answer": "Knowing theoretical concepts (intelligence) is useless without the practical execution and emotional control (wisdom) to make money.",
    "explanation": "🏗️ Khan: Theoretical finance is merely a prerequisite. True market outperformance requires the wisdom to execute strategies amidst systemic volatility. 🔥 Zara: You can memorize the whole textbook, but if you don't have the guts to act when the market bleeds, you won't make a dime!"
  },
  {
    "question": "At a macro level, how does the speaker define the structural nature of the stock market?",
    "options": [
      "A charity system designed to evenly distribute wealth among all citizens.",
      "A legal mechanism that transfers wealth from the uninformed, emotionally driven masses to the disciplined, informed minority.",
      "A fixed-income asset that acts exactly like a traditional bank deposit.",
      "A random number generator where absolutely no one can consistently make money."
    ],
    "answer": "A legal mechanism that transfers wealth from the uninformed, emotionally driven masses to the disciplined, informed minority.",
    "explanation": "🏗️ Khan: The market functions as an arbitrage mechanism between emotional reactivity and disciplined patience, legally reallocating capital. 🔥 Zara: It's the ultimate survival of the fittest! The big players feast on the panic of the 99% who trade on fear and greed!"
  },
  {
    "question": "How does the 'Shopkeeper' analogy apply to strategic equity investing?",
    "options": [
      "Buying and selling daily to ensure constant, non-stop cash flow.",
      "Only buying goods that are already highly priced to ensure premium quality.",
      "Buying quality assets at cheaper valuations and patiently holding them until market sentiment drives the price up for a profitable sale.",
      "Forcing customers to buy stocks regardless of the current economic condition."
    ],
    "answer": "Buying quality assets at cheaper valuations and patiently holding them until market sentiment drives the price up for a profitable sale.",
    "explanation": "🏗️ Khan: A strategic investor operates like a wholesaler—accumulating undervalued inventory during market pessimism and liquidating during periods of euphoria. 🔥 Zara: Buy the amazing stuff when it's on sale and wait for everyone else to want it! Let time do the heavy lifting while you cash in!"
  }
]

day2_data = [
  {
    "question": "What is a core difference between how retail traders and professional traders make buying decisions according to the speaker?",
    "options": [
      "Retail uses complex algorithms, while professionals guess.",
      "Retail follows tips and news, while professionals follow a strict framework and process.",
      "Retail focuses on long-term compounding, while professionals focus on short-term gains.",
      "Retail only buys government bonds, while professionals buy stocks."
    ],
    "answer": "Retail follows tips and news, while professionals follow a strict framework and process.",
    "explanation": "🏗️ Khan: Structural success requires a defined framework, not sentiment. Retailers fail because they operate on borrowed conviction and emotional impulses. 🔥 Zara: Stop treating the market like a casino! Tip-chasing is for amateurs; real players stick to a solid, tested process!"
  },
  {
    "question": "How is a 'Large Cap' company primarily defined in the provided context?",
    "options": [
      "The top 100 companies based on market capitalization.",
      "A company with more than 10,000 employees.",
      "Any company that has been in business for over 50 years.",
      "A company that only sells products internationally."
    ],
    "answer": "The top 100 companies based on market capitalization.",
    "explanation": "🏗️ Khan: Market capitalization mathematically categorizes companies. The top 100 represent the largest equity bases and usually exhibit lower structural volatility. 🔥 Zara: Large caps are the heavyweights of the market! They are the top 100 giants that give your portfolio a rock-solid foundation!"
  },
  {
    "question": "What analogy does the speaker use to describe the natural tendency of a fundamentally strong stock during a market crash?",
    "options": [
      "A sinking ship that cannot be salvaged.",
      "A rubber ball pushed deep underwater that will naturally bounce up when pressure is released.",
      "A kite flying high that loses its string.",
      "A train that has run out of fuel."
    ],
    "answer": "A rubber ball pushed deep underwater that will naturally bounce up when pressure is released.",
    "explanation": "🏗️ Khan: Intrinsic value acts as buoyancy. External macro pressures push prices down temporarily, but flawless fundamentals force an inevitable reversion to the mean. 🔥 Zara: If the company isn't broken, a market crash is just someone holding a beach ball underwater. Let go, and BOOM, it shoots right back up!"
  },
  {
    "question": "How does an increase in crude oil prices typically impact the broader economy and RBI's policy?",
    "options": [
      "It increases inflation, causing RBI to increase interest rates to reduce money circulation.",
      "It lowers inflation, causing RBI to decrease interest rates.",
      "It has no impact on inflation or RBI policies.",
      "It increases company profits, causing RBI to eliminate all taxes."
    ],
    "answer": "It increases inflation, causing RBI to increase interest rates to reduce money circulation.",
    "explanation": "🏗️ Khan: Crude price spikes increase input costs, driving systemic inflation. To cool the economy, the central bank (RBI) constricts liquidity by hiking interest rates. 🔥 Zara: Expensive oil means expensive everything! The RBI raises rates to cool down the spending party, which slows down corporate growth!"
  },
  {
    "question": "What indicates that a company has strong 'Pricing Power'?",
    "options": [
      "The ability to completely avoid taking any loans from banks.",
      "The ability to force the government to lower corporate taxes.",
      "The ability to always buy raw materials at a discount.",
      "The ability to increase product prices to cover rising raw material costs without losing customers."
    ],
    "answer": "The ability to increase product prices to cover rising raw material costs without losing customers.",
    "explanation": "🏗️ Khan: True business resilience is demonstrated when a company can pass inflationary input costs to the end consumer without experiencing demand destruction. 🔥 Zara: If your costs go up, and you can just charge your loyal customers more without them running away, you hold the ultimate power card!"
  },
  {
    "question": "How does the speaker view a company with high cash reserves taking a short-term loan (Virtual Debt)?",
    "options": [
      "It is a terrible sign and the stock should be sold immediately.",
      "It can be a smart business move to maintain compounding investments while managing short-term capital needs.",
      "It means the company is going bankrupt and cannot pay its employees.",
      "It is illegal under SEBI regulations."
    ],
    "answer": "It can be a smart business move to maintain compounding investments while managing short-term capital needs.",
    "explanation": "🏗️ Khan: Leverage isn't inherently negative. Utilizing low-interest short-term debt while preserving high-yield compounding assets is a sophisticated capital allocation strategy. 🔥 Zara: Why break your 12% compounding machine for a temporary cash need? Borrow cheap at 10% and keep your golden goose running!"
  },
  {
    "question": "Why does the speaker exclude government-owned companies from the core wealth-building portfolios (F4/E4)?",
    "options": [
      "They are notorious for frequent bankruptcies.",
      "Their primary goal is maintaining market equilibrium and public service rather than maximizing profit.",
      "They are not legally allowed to be traded on the National Stock Exchange.",
      "They only operate in the defense and military sectors."
    ],
    "answer": "Their primary goal is maintaining market equilibrium and public service rather than maximizing profit.",
    "explanation": "🏗️ Khan: Government entities prioritize macroeconomic stability and public welfare over shareholder wealth maximization, which limits exponential capital growth. 🔥 Zara: You can't expect massive profits from a company whose main job is to keep the public happy and prices low! We want wealth-builders, not charities!"
  },
  {
    "question": "If a company's revenue and profits are at an all-time high, but its stock price has fallen 24% due to external market panic, how should a strategic investor react?",
    "options": [
      "Sell the stock immediately because the market knows something the financial statements do not.",
      "Treat it as a clear buying opportunity because the underlying business value has grown while the price is discounted.",
      "Short the stock to make money on its continued decline.",
      "Wait until the stock hits an all-time low before starting fundamental research."
    ],
    "answer": "Treat it as a clear buying opportunity because the underlying business value has grown while the price is discounted.",
    "explanation": "🏗️ Khan: A divergence between expanding financial metrics (revenue/profit) and contracting stock prices creates a prime fundamental arbitrage opportunity. 🔥 Zara: The business is making record cash, but the stock is on sale? That's not a red flag; that's a VIP discount ticket! Buy the dip!"
  },
  {
    "question": "Why do large institutional investors (Mutual Funds/FIIs) eventually want the market to go up, despite temporarily driving prices down during panics?",
    "options": [
      "Because SEBI mandates that markets must close positive at the end of the financial year.",
      "Because their profit comes from a percentage of the Assets Under Management (AUM), which grows as market prices rise.",
      "Because they receive direct subsidies from the government when the market hits all-time highs.",
      "Because falling markets automatically trigger the liquidation of their entire firm."
    ],
    "answer": "Because their profit comes from a percentage of the Assets Under Management (AUM), which grows as market prices rise.",
    "explanation": "🏗️ Khan: Institutional revenue models are directly tied to AUM size. They may initiate short-term corrections for better entry points, but their structural imperative is a rising market. 🔥 Zara: The big sharks make money by charging fees on the total pie! A bigger pie means bigger fees, so they absolutely need the market to soar eventually!"
  },
  {
    "question": "What is the primary difference in wealth creation when shifting from a mutual fund's typical 15% CAGR to a disciplined strategic approach yielding 25% CAGR over 20 years?",
    "options": [
      "It simply doubles the final corpus amount.",
      "It mathematically guarantees zero volatility and zero drawdowns throughout the 20-year journey.",
      "It requires borrowing money to achieve the extra percentage points.",
      "It creates a massive multiplier effect, turning what would be a 3 crore corpus into a 13+ crore corpus from the same initial investments."
    ],
    "answer": "It creates a massive multiplier effect, turning what would be a 3 crore corpus into a 13+ crore corpus from the same initial investments.",
    "explanation": "🏗️ Khan: The mathematics of compounding dictates that marginal increases in CAGR over extended durations result in exponential, nonlinear wealth accumulation. 🔥 Zara: A tiny 10% bump in your yearly average doesn't just add a little cash; over 20 years, it's the difference between buying a nice car and buying the whole dealership!"
  }
]

full_quiz = day1_data + day2_data

if not os.path.exists('data'):
    os.makedirs('data')

with open('data/quiz.json', 'w', encoding='utf-8') as f:
    json.dump(full_quiz, f, indent=2, ensure_ascii=False)

with open('quiz_preview.txt', 'w', encoding='utf-8') as f:
    for i, q in enumerate(full_quiz):
        f.write(f"Q{i+1}: {q['question']}\n")
        for j, opt in enumerate(q['options']):
            f.write(f"  {chr(65+j)}) {opt}\n")
        f.write(f"Answer: {q['answer']}\n")
        f.write(f"Explanation: {q['explanation']}\n")
        f.write('-' * 40 + '\n')

print("Success: data/quiz.json and quiz_preview.txt created.")
