---
layout: default
title: AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation
---

# AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16103" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16103v1</a>
  <a href="https://arxiv.org/pdf/2512.16103.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16103v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16103v1', 'AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sandeep Neela

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

**备注**: Preprint

---

## 💡 一句话要点

**AIMM：一种AI驱动的多模态框架，用于检测社交媒体影响的股市操纵**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `股市操纵检测` `社交媒体分析` `多模态融合` `风险评估` `机器学习`

## 📋 核心要点

1. 现有方法难以有效关联社交媒体叙事、协同模式与市场行为，从而难以检测股市操纵。
2. AIMM框架融合Reddit活动、机器人指标和市场特征，生成每日操纵风险评分，辅助分析师识别可疑行为。
3. 实验表明，AIMM具有初步的区分能力，并在GME事件发生前22天发出预警，展示了其潜在的应用价值。

## 📝 摘要（中文）

本文提出AIMM，一个AI驱动的框架，旨在融合Reddit活动、机器人和协同行为指标以及OHLCV市场特征，为每个股票代码生成每日AIMM操纵风险评分。该系统采用基于Parquet的流水线，并配备Streamlit仪表板，使分析师能够探索可疑窗口，检查底层帖子和价格行为，并记录模型随时间推移的输出。由于Reddit API的限制，我们使用了经过校准的合成社交特征，以匹配已记录的事件特征；市场数据（OHLCV）使用来自Yahoo Finance的真实历史数据。本文贡献包括：构建AIMM Ground Truth数据集（AIMM-GT），包含33个标记的股票代码-天，涵盖8个股票，数据来自SEC执法行动、社区验证的操纵案例和匹配的正常对照；实施前向步进评估和前瞻性预测日志记录，用于回顾性和部署式评估；分析提前期，结果表明AIMM在2021年1月GME挤兑高峰前22天发出了警告。尽管当前标记集较小，但结果显示了初步的区分能力和对GME事件的早期预警。我们发布代码、数据集模式和仪表板设计，以支持对社交媒体驱动的市场监控的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决社交媒体影响下股市操纵行为的检测问题。现有方法难以将社交媒体上的叙事、协同模式与市场行为有效关联，导致无法及时发现和预警操纵行为。零售投资者、监管机构和经纪公司需要能够连接在线叙事和协同模式与市场行为的工具。

**核心思路**：论文的核心思路是利用AI技术，融合来自不同模态的数据（社交媒体活动、机器人行为指标、市场交易数据），构建一个综合的风险评估体系。通过分析这些数据的关联性，可以更准确地识别潜在的股市操纵行为。这种多模态融合的方法能够弥补单一数据源的局限性，提高检测的准确性和可靠性。

**技术框架**：AIMM框架包含以下主要模块：1) 数据收集与预处理：收集Reddit数据、机器人行为指标和OHLCV市场数据，并进行清洗和预处理。由于Reddit API限制，使用校准的合成社交特征。2) 特征工程：从收集的数据中提取相关特征，例如Reddit帖子的情感、机器人账户的活跃度、交易量和价格波动等。3) 模型训练：使用机器学习模型（具体模型类型未知）将提取的特征映射到操纵风险评分。4) 风险评估与预警：根据模型输出的风险评分，生成每日AIMM操纵风险评分，并设置阈值进行预警。5) 可视化与分析：通过Streamlit仪表板，分析师可以探索可疑窗口，检查底层帖子和价格行为，并记录模型输出。

**关键创新**：AIMM的关键创新在于其多模态融合的框架，能够综合考虑社交媒体、机器人行为和市场交易数据，从而更全面地评估股市操纵风险。此外，AIMM还构建了一个包含标记数据的AIMM-GT数据集，并实现了前向步进评估和前瞻性预测日志记录，为模型评估和部署提供了支持。

**关键设计**：由于论文摘要中没有提供关于关键参数设置、损失函数、网络结构等技术细节，因此这部分信息未知。但可以推测，模型训练可能采用了监督学习方法，损失函数可能与分类或回归任务相关。合成社交特征的校准方法也是一个关键设计，旨在模拟真实的社交媒体行为。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16103v1/figures/GroundTruthCoverage.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16103v1/figures/Forward-walk.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16103v1/figures/PredictionLog.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AIMM具有初步的区分能力，能够识别潜在的股市操纵行为。特别值得一提的是，AIMM在2021年1月GME挤兑高峰前22天发出了预警，展示了其在早期预警方面的潜力。尽管当前标记集较小，但这些结果表明AIMM具有实际应用价值，并为未来的研究提供了方向。

## 🎯 应用场景

AIMM框架可应用于金融监管、风险管理和投资决策等领域。监管机构可以使用AIMM来监控市场操纵行为，及时采取措施保护投资者利益。经纪公司可以利用AIMM来评估客户交易的风险，并提供个性化的投资建议。零售投资者可以使用AIMM来识别潜在的投资风险，做出更明智的投资决策。该研究有助于提升市场透明度和公平性，维护金融市场的稳定。

## 📄 摘要（原文）

> Market manipulation now routinely originates from coordinated social media campaigns, not isolated trades. Retail investors, regulators, and brokerages need tools that connect online narratives and coordination patterns to market behavior. We present AIMM, an AI-driven framework that fuses Reddit activity, bot and coordination indicators, and OHLCV market features into a daily AIMM Manipulation Risk Score for each ticker.
>   The system uses a parquet-native pipeline with a Streamlit dashboard that allows analysts to explore suspicious windows, inspect underlying posts and price action, and log model outputs over time. Due to Reddit API restrictions, we employ calibrated synthetic social features matching documented event characteristics; market data (OHLCV) uses real historical data from Yahoo Finance. This release makes three contributions. First, we build the AIMM Ground Truth dataset (AIMM-GT): 33 labeled ticker-days spanning eight equities, drawing from SEC enforcement actions, community-verified manipulation cases, and matched normal controls. Second, we implement forward-walk evaluation and prospective prediction logging for both retrospective and deployment-style assessment. Third, we analyze lead times and show that AIMM flagged GME 22 days before the January 2021 squeeze peak.
>   The current labeled set is small (33 ticker-days, 3 positive events), but results show preliminary discriminative capability and early warnings for the GME incident. We release the code, dataset schema, and dashboard design to support research on social media-driven market surveillance.

