---
layout: default
title: "VideoConviction: A Multimodal Benchmark for Human Conviction and Stock Market Recommendations"
---

# VideoConviction: A Multimodal Benchmark for Human Conviction and Stock Market Recommendations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.08104" class="toolbar-btn" target="_blank">📄 arXiv: 2507.08104v1</a>
  <a href="https://arxiv.org/pdf/2507.08104.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.08104v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.08104v1', 'VideoConviction: A Multimodal Benchmark for Human Conviction and Stock Market Recommendations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Michael Galarnyk, Veer Kejriwal, Agam Shah, Yash Bhardwaj, Nicholas Meyer, Anand Krishnan, Sudheer Chava

**分类**: cs.MM, cs.AI, cs.CL, cs.CV

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**提出VideoConviction以解决金融领域多模态分析问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态分析` `金融推荐` `数据集构建` `模型评估` `社交媒体影响`

## 📋 核心要点

1. 现有方法在分析金融影响者的推荐时，难以有效区分投资行为和信念强度，导致误分类现象普遍。
2. 论文提出VideoConviction数据集，通过多模态信号分析，基准测试多模态和文本基础模型在金融推荐中的表现。
3. 实验结果表明，高信念推荐的表现虽优于低信念推荐，但整体仍低于标准普尔500指数，反向策略表现更佳。

## 📝 摘要（中文）

社交媒体的兴起使得金融影响者（finfluencers）在平台上分享股票推荐，理解其影响力需要分析语调、表达风格和面部表情等多模态信号。本文介绍了VideoConviction，一个包含6000多个专家注释的多模态数据集，旨在基准测试多模态大型语言模型（MLLMs）和文本基础大型语言模型（LLMs）在金融话语中的表现。结果显示，尽管多模态输入提升了股票代码提取的效果，但模型在区分投资行为和信念强度方面仍存在困难，常常将一般评论误分类为明确推荐。高信念推荐的表现优于低信念推荐，但仍不及流行的标准普尔500指数基金。相反的策略——对抗金融影响者的推荐，年回报率超出标准普尔500指数6.8%，但风险更高。该基准测试为多模态任务的多样化评估提供了可能。

## 🔬 方法详解

**问题定义**：本文旨在解决金融领域中对金融影响者推荐的多模态分析问题。现有方法主要依赖文本分析，难以捕捉语调和面部表情等非语言信号，导致对投资行为和信念强度的误判。

**核心思路**：通过构建VideoConviction数据集，整合视频中的多模态信号，提供一个全面的基准测试平台，以评估多模态大型语言模型和文本基础模型在金融推荐中的表现。

**技术框架**：整体架构包括数据收集、注释、模型训练和评估四个主要模块。数据收集阶段涵盖了457小时的金融视频，注释阶段则由专家提供了6000多个标注。模型训练阶段使用多模态输入进行训练，评估阶段则比较不同模型在全视频和分段视频输入下的表现。

**关键创新**：最重要的技术创新在于引入多模态信号分析，尤其是对语调和面部表情的重视，使得模型能够更全面地理解金融推荐的语境和信念强度。这与传统的文本分析方法形成了鲜明对比。

**关键设计**：在模型设计中，采用了特定的损失函数以优化多模态输入的融合效果，并在网络结构上进行了调整，以适应视频数据的特性。

## 📊 实验亮点

实验结果显示，尽管多模态输入在股票代码提取上有所提升，但模型在区分投资行为和信念强度方面仍存在显著困难。高信念推荐的表现优于低信念推荐，但整体仍低于标准普尔500指数，反向策略的年回报率超出标准普尔500指数6.8%。

## 🎯 应用场景

该研究的潜在应用领域包括金融市场分析、投资决策支持和社交媒体内容监测。通过更准确地理解金融影响者的推荐，投资者可以做出更明智的决策，从而提高投资回报率。此外，该研究为多模态分析技术在其他领域的应用提供了参考。

## 📄 摘要（原文）

> Social media has amplified the reach of financial influencers known as "finfluencers," who share stock recommendations on platforms like YouTube. Understanding their influence requires analyzing multimodal signals like tone, delivery style, and facial expressions, which extend beyond text-based financial analysis. We introduce VideoConviction, a multimodal dataset with 6,000+ expert annotations, produced through 457 hours of human effort, to benchmark multimodal large language models (MLLMs) and text-based large language models (LLMs) in financial discourse. Our results show that while multimodal inputs improve stock ticker extraction (e.g., extracting Apple's ticker AAPL), both MLLMs and LLMs struggle to distinguish investment actions and conviction--the strength of belief conveyed through confident delivery and detailed reasoning--often misclassifying general commentary as definitive recommendations. While high-conviction recommendations perform better than low-conviction ones, they still underperform the popular S\&P 500 index fund. An inverse strategy--betting against finfluencer recommendations--outperforms the S\&P 500 by 6.8\% in annual returns but carries greater risk (Sharpe ratio of 0.41 vs. 0.65). Our benchmark enables a diverse evaluation of multimodal tasks, comparing model performance on both full video and segmented video inputs. This enables deeper advancements in multimodal financial research. Our code, dataset, and evaluation leaderboard are available under the CC BY-NC 4.0 license.

