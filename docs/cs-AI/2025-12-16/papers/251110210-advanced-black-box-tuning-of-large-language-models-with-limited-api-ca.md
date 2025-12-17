---
layout: default
title: Advanced Black-Box Tuning of Large Language Models with Limited API Calls
---

# Advanced Black-Box Tuning of Large Language Models with Limited API Calls

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10210" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10210</a>
  <a href="https://arxiv.org/pdf/2511.10210.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10210" onclick="toggleFavorite(this, '2511.10210', 'Advanced Black-Box Tuning of Large Language Models with Limited API Calls')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhikang Xie, Weilin Wan, Peizhu Gong, Weizhong Zhang, Cheng Jin

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出一种高级黑盒调优方法，以有限API调用高效优化大语言模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `黑盒调优` `大语言模型` `高斯过程` `代理模型` `API调用` `模型适配` `LogitMap Pairs`

## 📋 核心要点

1. 现有黑盒调优方法在效率和性能之间存在权衡，要么效率高但提升有限，要么性能好但API调用成本过高。
2. 该论文提出使用高斯过程（GP）代理模型，通过少量API调用学习基础模型的行为，指导代理模型的训练。
3. 实验表明，该方法在显著降低API调用次数的同时，将模型准确率从55.92%提升至86.85%，优于离线方法。

## 📝 摘要（中文）

黑盒调优是一种新兴范式，用于调整大型语言模型（LLM）以更好地实现期望的行为，尤其是在无法直接访问模型参数时。然而，当前的策略常常面临次优的极端困境：要么单独训练一个小型的代理模型，然后用它来改变基础模型的预测，这种方法效率显著，但改进有限；要么在每个调优迭代中对基础模型进行API调用，这会带来过高的计算成本。因此，我们提出了一种针对LLM的高级黑盒调优方法，该方法限制了API调用次数。我们的核心策略包括训练一个高斯过程（GP）代理模型，该模型使用从基础模型查询获得的“LogitMap Pairs”，这些查询基于一个最小但信息量极高的训练子集。该代理模型可以近似基础模型的输出，从而指导代理模型的训练，有效地减少了对基础模型直接查询的需求。大量实验验证了我们的方法将预训练语言模型的准确率从55.92%提高到86.85%，并将API查询频率降低到仅1.38%。这显著优于完全无需API访问的离线方法。值得注意的是，我们的方法在显著降低API成本的同时，也实现了与查询密集型方法相当或更高的准确率。这为语言模型适配提供了一种稳健且高效的范式。

## 🔬 方法详解

**问题定义**：现有黑盒调优方法在调整大型语言模型时面临效率和性能的困境。直接对基础模型进行API调用成本高昂，而离线训练代理模型效果有限。因此，需要一种在有限API调用的情况下，有效提升模型性能的黑盒调优方法。

**核心思路**：核心思路是利用高斯过程（GP）构建一个代理模型，该模型能够近似基础模型的输出。通过少量但信息量大的API调用，学习基础模型的“LogitMap Pairs”，然后利用这些信息训练GP代理模型。该代理模型随后用于指导代理模型的训练，从而减少对基础模型直接查询的需求。

**技术框架**：整体框架包含以下几个主要阶段：1) 使用少量API调用查询基础模型，获取“LogitMap Pairs”；2) 利用“LogitMap Pairs”训练高斯过程（GP）代理模型；3) 使用GP代理模型指导代理模型的训练；4) 使用训练好的代理模型进行预测。

**关键创新**：关键创新在于使用高斯过程（GP）作为代理模型，并利用“LogitMap Pairs”进行训练。这种方法能够在少量API调用的情况下，有效地学习基础模型的行为，从而指导代理模型的训练。与现有方法相比，该方法在API调用成本和模型性能之间取得了更好的平衡。

**关键设计**：论文中关键的设计包括：如何选择最具信息量的训练子集以减少API调用次数；如何构建和训练高斯过程（GP）代理模型；以及如何利用GP代理模型指导代理模型的训练。具体的参数设置和损失函数等技术细节在论文中进行了详细描述（具体数值未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.10210/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.10210/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.10210/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在将预训练语言模型的准确率从55.92%提升到86.85%的同时，将API查询频率降低到仅1.38%。这显著优于完全无需API访问的离线方法，并且在API成本显著降低的情况下，实现了与查询密集型方法相当或更高的准确率。这些结果验证了该方法在黑盒调优方面的有效性和高效性。

## 🎯 应用场景

该研究成果可应用于各种需要对大型语言模型进行定制化调整的场景，例如特定领域的文本生成、对话系统优化、以及模型行为的干预和控制。该方法降低了API调用成本，使得在资源受限的环境下也能高效地进行模型调优，具有广泛的应用前景和实际价值。未来，该方法可以进一步扩展到其他类型的黑盒模型调优任务。

## 📄 摘要（原文）

> Black-box tuning is an emerging paradigm for adapting large language models (LLMs) to better achieve desired behaviors, particularly when direct access to model parameters is unavailable. Current strategies, however, often present a dilemma of suboptimal extremes: either separately train a small proxy model and then use it to shift the predictions of the foundation model, offering notable efficiency but often yielding limited improvement; or making API calls in each tuning iteration to the foundation model, which entails prohibitive computational costs. Therefore, we propose a novel advanced black-box tuning method for LLMs with limited API calls. Our core strategy involves training a Gaussian Process (GP) surrogate model with "LogitMap Pairs" derived from querying the foundation model on a minimal but highly informative training subset. This surrogate can approximate the outputs of the foundation model to guide the training of the proxy model, thereby effectively reducing the need for direct queries to the foundation model. Extensive experiments verify that our approach elevates pre-trained language model accuracy from 55.92% to 86.85%, reducing the frequency of API queries to merely 1.38%. This significantly outperforms offline approaches that operate entirely without API access. Notably, our method also achieves comparable or superior accuracy to query-intensive approaches, while significantly reducing API costs. This offers a robust and high-efficiency paradigm for language model adaptation.

