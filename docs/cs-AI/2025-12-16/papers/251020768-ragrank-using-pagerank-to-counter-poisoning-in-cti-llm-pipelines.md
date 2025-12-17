---
layout: default
title: RAGRank: Using PageRank to Counter Poisoning in CTI LLM Pipelines
---

# RAGRank: Using PageRank to Counter Poisoning in CTI LLM Pipelines

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20768" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20768</a>
  <a href="https://arxiv.org/pdf/2510.20768.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20768" onclick="toggleFavorite(this, '2510.20768', 'RAGRank: Using PageRank to Counter Poisoning in CTI LLM Pipelines')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Austin Jia, Avaneesh Ramesh, Zain Shamsi, Daniel Zhang, Alex Liu

**分类**: cs.CR, cs.AI, cs.IR

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**RAGRank：利用PageRank提升CTI LLM流水线抗投毒攻击能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `大型语言模型` `网络威胁情报` `投毒攻击` `PageRank` `来源可信度` `信息安全`

## 📋 核心要点

1. 现有的RAG系统在CTI领域面临投毒攻击的挑战，因为新兴威胁信息新颖且攻击者能模仿合法内容。
2. 论文提出使用PageRank等来源可信度算法，对RAG系统的知识库进行评估，从而降低恶意文档的影响。
3. 实验结果表明，该方法能有效降低恶意文档的权威评分，同时提升可信内容的权重，增强RAG系统的鲁棒性。

## 📝 摘要（中文）

检索增强生成(RAG)已成为在网络威胁情报(CTI)系统中应用大型语言模型(LLM)的主流架构模式。然而，这种设计容易受到投毒攻击。先前提出的防御方法在CTI环境中可能会失效，因为网络威胁信息对于新兴攻击而言通常是全新的，并且复杂的威胁参与者可以模仿合法的格式、术语和文体习惯。为了解决这个问题，我们提出通过在语料库上应用来源可信度算法（以PageRank为例）来加速现代RAG防御的鲁棒性。在我们的实验中，我们定量地证明了我们的算法降低了恶意文档的权威评分，同时提升了可信内容，使用了标准化的MS MARCO数据集。我们还展示了我们的算法在CTI文档和信息源上的概念验证性能。

## 🔬 方法详解

**问题定义**：论文旨在解决CTI系统中，基于RAG的LLM应用易受投毒攻击的问题。现有的防御方法无法有效应对CTI场景，因为威胁情报具有时效性和新颖性，攻击者可以伪装成合法的来源和格式，使得传统的检测方法失效。

**核心思路**：核心思路是利用来源可信度算法，对RAG系统使用的知识库进行评估和排序。通过降低恶意来源的权重，提高可信来源的权重，从而减少投毒攻击对LLM生成结果的影响。PageRank算法被用作来源可信度评估的一个具体例子。

**技术框架**：整体框架是在RAG流水线中，在检索阶段之前，对文档进行预处理，计算每个文档的PageRank值。PageRank值反映了文档在知识图谱中的重要性和可信度。在检索阶段，文档会根据其PageRank值进行排序，优先选择PageRank值高的文档。LLM则基于排序后的文档生成最终的答案。

**关键创新**：关键创新在于将来源可信度评估引入到RAG的防御体系中，特别是在CTI领域。与传统的基于内容过滤或异常检测的方法不同，该方法关注的是文档的来源，而不是文档的内容本身，因此可以更好地应对攻击者伪装成合法来源的情况。

**关键设计**：论文使用PageRank算法作为来源可信度评估的具体实现。PageRank算法需要构建一个文档之间的链接图，其中链接表示文档之间的引用关系。算法的关键参数包括阻尼因子（damping factor）和迭代次数。阻尼因子控制了随机跳转的概率，迭代次数决定了算法的收敛速度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.20768/images/RAGRank-architecture.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.20768/images/msmarco_accuracy.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.20768/images/chunk_analysis.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RAGRank算法能够有效降低恶意文档的权威评分，同时提升可信内容的权重。在MS MARCO数据集上进行了定量评估，证明了该算法的有效性。此外，还在CTI文档和信息源上进行了概念验证，展示了该算法在实际应用中的潜力。具体的性能数据和提升幅度在论文中进行了详细的展示。

## 🎯 应用场景

该研究成果可应用于各种网络安全场景，例如威胁情报分析、漏洞管理、安全事件响应等。通过提高RAG系统的抗投毒能力，可以更可靠地利用LLM进行安全分析和决策，降低因恶意信息误导而造成的风险。未来，该方法可以扩展到其他领域，例如金融风控、舆情分析等，提升信息系统的安全性。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) has emerged as the dominant architectural pattern to operationalize Large Language Model (LLM) usage in Cyber Threat Intelligence (CTI) systems. However, this design is susceptible to poisoning attacks, and previously proposed defenses can fail for CTI contexts as cyber threat information is often completely new for emerging attacks, and sophisticated threat actors can mimic legitimate formats, terminology, and stylistic conventions. To address this issue, we propose that the robustness of modern RAG defenses can be accelerated by applying source credibility algorithms on corpora, using PageRank as an example. In our experiments, we demonstrate quantitatively that our algorithm applies a lower authority score to malicious documents while promoting trusted content, using the standardized MS MARCO dataset. We also demonstrate proof-of-concept performance of our algorithm on CTI documents and feeds.

