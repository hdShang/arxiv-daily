---
layout: default
title: "AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation"
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

**AIMM：用于检测社交媒体影响的股票市场操纵的人工智能驱动多模态框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `市场操纵检测` `社交媒体分析` `多模态融合` `风险预警` `人工智能` `股票市场` `机器人检测`

## 📋 核心要点

1. 现有市场操纵检测方法难以有效关联社交媒体叙事与市场行为，缺乏对在线协调模式的分析。
2. AIMM框架融合Reddit活动、机器人指标、协调模式和市场特征，生成每日操纵风险评分，提供早期预警。
3. 实验表明，AIMM在小规模数据集上具有初步区分能力，并在GME事件发生前22天成功发出预警。

## 📝 摘要（中文）

市场操纵现在通常源于有组织的社交媒体活动，而非孤立的交易行为。零售投资者、监管机构和经纪公司需要能够将在线叙事和协调模式与市场行为联系起来的工具。我们提出了AIMM，一个人工智能驱动的框架，它将Reddit活动、机器人和协调指标以及OHLCV市场特征融合为每个股票代码的每日AIMM操纵风险评分。该系统使用一个parquet原生管道和一个Streamlit仪表板，分析师可以通过它来探索可疑窗口，检查底层帖子和价格行为，并记录随时间推移的模型输出。由于Reddit API的限制，我们采用了经过校准的合成社交特征，以匹配已记录的事件特征；市场数据（OHLCV）使用来自Yahoo Finance的真实历史数据。这项工作有三个贡献。首先，我们构建了AIMM Ground Truth数据集（AIMM-GT）：33个标记的股票代码-天，涵盖8个股票，数据来自SEC的执法行动、社区验证的操纵案例和匹配的正常对照。其次，我们为回顾性和部署式评估实施了前向步进评估和前瞻性预测日志记录。第三，我们分析了提前期，并表明AIMM在2021年1月GME挤兑高峰前22天发出了警告。当前的标记集很小（33个股票代码-天，3个正面事件），但结果显示了初步的区分能力和对GME事件的早期警告。我们发布了代码、数据集模式和仪表板设计，以支持对社交媒体驱动的市场监控的研究。

## 🔬 方法详解

**问题定义**：当前市场操纵行为日益依赖社交媒体的协调活动，传统方法难以有效识别。零售投资者和监管机构缺乏将社交媒体叙事与市场行为关联的工具，无法及时发现和应对潜在的操纵风险。现有方法未能充分利用社交媒体数据中的信息，缺乏对机器人行为和协调模式的有效分析。

**核心思路**：AIMM的核心思路是将社交媒体数据（Reddit活动）、机器人和协调指标以及传统的市场数据（OHLCV）进行融合，利用人工智能技术学习这些数据之间的关联，从而识别潜在的市场操纵行为。通过计算每日的AIMM操纵风险评分，为投资者和监管机构提供早期预警。这种多模态融合的方法能够更全面地捕捉市场操纵的迹象。

**技术框架**：AIMM框架包含以下主要模块：1) 数据收集模块：收集Reddit数据、市场数据（OHLCV）以及机器人和协调指标。由于Reddit API的限制，使用校准后的合成社交特征。2) 特征工程模块：从收集到的数据中提取相关特征，例如Reddit帖子的情感、机器人活动频率、价格波动率等。3) 模型训练模块：使用机器学习模型（具体模型类型未知）学习特征与市场操纵之间的关系。4) 风险评分计算模块：根据模型输出计算每日的AIMM操纵风险评分。5) 可视化仪表板：使用Streamlit构建仪表板，方便分析师探索可疑窗口，检查底层帖子和价格行为。

**关键创新**：AIMM的关键创新在于其多模态数据融合的方法，将社交媒体数据、机器人指标和市场数据结合起来，从而更全面地捕捉市场操纵的迹象。此外，AIMM还构建了AIMM-GT数据集，为市场操纵检测研究提供了宝贵的资源。前向步进评估和前瞻性预测日志记录方法也为模型的评估和部署提供了更可靠的手段。

**关键设计**：论文中没有详细描述具体的模型结构、损失函数或参数设置。由于Reddit API限制，使用了校准的合成社交特征，具体的校准方法未知。AIMM-GT数据集包含33个标记的股票代码-天，其中3个为正面事件，数据集规模较小。

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

AIMM在包含33个标记股票代码-天的小规模数据集上展现了初步的区分能力。最重要的是，AIMM在2021年1月GME挤兑高峰前22天发出了预警，表明其具有早期预警的潜力。研究团队发布了代码、数据集模式和仪表板设计，为进一步研究社交媒体驱动的市场监控提供了基础。

## 🎯 应用场景

AIMM框架可应用于股票市场监管、风险管理和投资决策。监管机构可以使用AIMM来监控社交媒体上的市场操纵活动，及时采取行动。经纪公司可以使用AIMM来评估客户交易的风险，并提供更安全的投资环境。零售投资者可以使用AIMM来识别潜在的投资风险，做出更明智的决策。该研究有助于提高市场透明度和公平性。

## 📄 摘要（原文）

> Market manipulation now routinely originates from coordinated social media campaigns, not isolated trades. Retail investors, regulators, and brokerages need tools that connect online narratives and coordination patterns to market behavior. We present AIMM, an AI-driven framework that fuses Reddit activity, bot and coordination indicators, and OHLCV market features into a daily AIMM Manipulation Risk Score for each ticker.
>   The system uses a parquet-native pipeline with a Streamlit dashboard that allows analysts to explore suspicious windows, inspect underlying posts and price action, and log model outputs over time. Due to Reddit API restrictions, we employ calibrated synthetic social features matching documented event characteristics; market data (OHLCV) uses real historical data from Yahoo Finance. This release makes three contributions. First, we build the AIMM Ground Truth dataset (AIMM-GT): 33 labeled ticker-days spanning eight equities, drawing from SEC enforcement actions, community-verified manipulation cases, and matched normal controls. Second, we implement forward-walk evaluation and prospective prediction logging for both retrospective and deployment-style assessment. Third, we analyze lead times and show that AIMM flagged GME 22 days before the January 2021 squeeze peak.
>   The current labeled set is small (33 ticker-days, 3 positive events), but results show preliminary discriminative capability and early warnings for the GME incident. We release the code, dataset schema, and dashboard design to support research on social media-driven market surveillance.

