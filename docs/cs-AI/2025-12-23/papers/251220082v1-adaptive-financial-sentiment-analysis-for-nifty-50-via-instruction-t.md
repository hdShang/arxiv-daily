---
layout: default
title: Adaptive Financial Sentiment Analysis for NIFTY 50 via Instruction-Tuned LLMs , RAG and Reinforcement Learning Approaches
---

# Adaptive Financial Sentiment Analysis for NIFTY 50 via Instruction-Tuned LLMs , RAG and Reinforcement Learning Approaches

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20082" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20082v1</a>
  <a href="https://arxiv.org/pdf/2512.20082.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20082v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20082v1', 'Adaptive Financial Sentiment Analysis for NIFTY 50 via Instruction-Tuned LLMs , RAG and Reinforcement Learning Approaches')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaithra, Kamesh Kadimisetty, Biju R Mohan

**分类**: cs.AI

**发布日期**: 2025-12-23

**备注**: Accepted in CODS 2025

---

## 💡 一句话要点

**提出基于指令调优LLM、RAG和强化学习的自适应金融情感分析框架，用于NIFTY 50指数预测。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `金融情感分析` `指令调优LLM` `检索增强生成` `强化学习` `股票市场预测` `自适应模型` `NIFTY 50`

## 📋 核心要点

1. 现有金融情感分析方法忽略了股票价格和市场反馈对情感分析的影响，导致预测精度受限。
2. 提出一种自适应框架，结合指令调优的LLM、RAG和强化学习，利用市场反馈动态调整情感分析模型。
3. 实验结果表明，该系统在NIFTY 50新闻标题情感分析中，显著提高了分类准确率、F1分数和市场对齐度。

## 📝 摘要（中文）

金融情感分析在投资决策、市场风险评估和股票价格趋势预测中起着至关重要的作用。现有金融情感分析工作尚未考虑股票价格或市场反馈对情感分析的影响。本文提出了一个自适应框架，该框架将大型语言模型（LLM）与真实股票市场反馈相结合，以提高印度股票市场背景下的情感分类性能。该方法使用基于指令的学习在SentiFin数据集上微调LLaMA 3.2 3B模型。为了增强情感预测，采用检索增强生成（RAG）流程，该流程基于句子嵌入的余弦相似度动态选择多源上下文信息。此外，引入了一个反馈驱动模块，通过比较预测的情感与实际的次日股票收益来调整来源的可靠性，使系统能够迭代地适应市场行为。为了在时间数据上推广这种自适应机制，引入了一个使用近端策略优化（PPO）训练的强化学习代理。PPO代理学习基于情感-收益对齐的累积奖励信号来优化来源加权策略。对2024年至2025年收集的NIFTY 50新闻标题进行的实验结果表明，所提出的系统显著提高了分类准确率、F1分数和市场对齐度，优于基线模型和静态检索方法。结果验证了将指令调优的LLM与动态反馈和强化学习相结合以实现稳健的、市场感知的金融情感建模的潜力。

## 🔬 方法详解

**问题定义**：现有金融情感分析方法未能充分利用股票市场反馈信息，导致情感分析结果与实际市场表现的关联性较弱，无法有效指导投资决策。这些方法通常是静态的，无法适应不断变化的市场动态。

**核心思路**：本文的核心思路是构建一个自适应的情感分析框架，该框架能够从实际股票市场反馈中学习，并动态调整情感分析模型，使其更好地适应市场行为。通过将LLM与RAG和强化学习相结合，实现对市场信息的有效利用和对模型参数的动态优化。

**技术框架**：该框架包含以下主要模块：1) 指令调优的LLM：使用SentiFin数据集对LLaMA 3.2 3B模型进行指令调优，以提高情感分类能力。2) RAG：利用RAG流程，基于句子嵌入的余弦相似度动态选择多源上下文信息，增强情感预测。3) 反馈驱动模块：通过比较预测情感与实际次日股票收益，调整信息来源的可靠性。4) 强化学习代理：使用PPO算法训练强化学习代理，优化信息来源的加权策略，以适应市场变化。

**关键创新**：该方法最重要的创新点在于其自适应性，能够根据市场反馈动态调整情感分析模型。通过强化学习，系统能够学习最优的信息来源加权策略，从而提高情感分析的准确性和市场对齐度。与现有静态方法相比，该方法能够更好地适应市场动态变化。

**关键设计**：在RAG模块中，使用余弦相似度来衡量句子嵌入之间的相似性，从而选择相关的上下文信息。在强化学习模块中，使用PPO算法训练代理，奖励信号基于情感预测与实际股票收益的对齐程度。具体参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20082v1/Methodology.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20082v1/initial_source_weights.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20082v1/ppo_source_weights.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该系统在NIFTY 50新闻标题情感分析中，显著提高了分类准确率、F1分数和市场对齐度，优于基线模型和静态检索方法。具体的性能提升数据未在摘要中给出，属于未知信息。该结果验证了将指令调优的LLM与动态反馈和强化学习相结合的有效性。

## 🎯 应用场景

该研究成果可应用于智能投资顾问、风险管理系统和量化交易策略等领域。通过更准确地分析市场情绪，可以帮助投资者做出更明智的决策，降低投资风险，提高投资回报。该方法还可用于构建更稳健的市场监控系统，及时发现潜在的市场风险。

## 📄 摘要（原文）

> Financial sentiment analysis plays a crucial role in informing investment decisions, assessing market risk, and predicting stock price trends. Existing works in financial sentiment analysis have not considered the impact of stock prices or market feedback on sentiment analysis. In this paper, we propose an adaptive framework that integrates large language models (LLMs) with real-world stock market feedback to improve sentiment classification in the context of the Indian stock market. The proposed methodology fine-tunes the LLaMA 3.2 3B model using instruction-based learning on the SentiFin dataset. To enhance sentiment predictions, a retrieval-augmented generation (RAG) pipeline is employed that dynamically selects multi-source contextual information based on the cosine similarity of the sentence embeddings. Furthermore, a feedback-driven module is introduced that adjusts the reliability of the source by comparing predicted sentiment with actual next-day stock returns, allowing the system to iteratively adapt to market behavior. To generalize this adaptive mechanism across temporal data, a reinforcement learning agent trained using proximal policy optimization (PPO) is incorporated. The PPO agent learns to optimize source weighting policies based on cumulative reward signals from sentiment-return alignment. Experimental results on NIFTY 50 news headlines collected from 2024 to 2025 demonstrate that the proposed system significantly improves classification accuracy, F1-score, and market alignment over baseline models and static retrieval methods. The results validate the potential of combining instruction-tuned LLMs with dynamic feedback and reinforcement learning for robust, market-aware financial sentiment modeling.

