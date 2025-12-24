---
layout: default
title: "Better with Less: Small Proprietary Models Surpass Large Language Models in Financial Transaction Understanding"
---

# Better with Less: Small Proprietary Models Surpass Large Language Models in Financial Transaction Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25803" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25803v1</a>
  <a href="https://arxiv.org/pdf/2509.25803.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25803v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25803v1', 'Better with Less: Small Proprietary Models Surpass Large Language Models in Financial Transaction Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wanying Ding, Savinay Narendra, Xiran Shi, Adwait Ratnaparkhi, Chengrui Yang, Nikoo Sabzevar, Ziyan Yin

**分类**: cs.IR, cs.AI, cs.CE, cs.LG

**发布日期**: 2025-09-30

**备注**: 9 pages, 5 figures

---

## 💡 一句话要点

**小规模金融交易专属模型超越大型语言模型，提升交易理解能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `金融交易理解` `Transformer模型` `专有模型` `领域自适应` `Decoder-Only模型` `成本效益` `欺诈检测`

## 📋 核心要点

1. 现有大型语言模型在金融交易理解方面表现不佳，无法满足实时性和成本效益的需求。
2. 论文提出定制化的小规模专有模型，针对金融交易数据的特性进行优化，提升性能。
3. 实验表明，专有模型在速度和成本上优于大型语言模型，并提升了交易覆盖率。

## 📝 摘要（中文）

分析金融交易对于确保合规、检测欺诈和支持决策至关重要。金融交易数据的复杂性需要先进的技术来提取有意义的见解并确保准确的分析。由于基于Transformer的模型在多个领域表现出色，本文旨在探索它们在理解金融交易方面的潜力。本文进行了广泛的实验，以评估三种类型的Transformer模型：Encoder-Only、Decoder-Only和Encoder-Decoder模型。对于每种类型，我们探索了三个选项：预训练的LLM、微调的LLM和从头开始开发的小型专有模型。我们的分析表明，虽然LLM（如LLaMA3-8b、Flan-T5和SBERT）在各种自然语言处理任务中表现出令人印象深刻的能力，但在金融交易理解的特定背景下，它们并没有明显优于小型专有模型。这种现象在速度和成本效率方面尤为明显。专有模型针对交易数据的独特需求量身定制，表现出更快的处理速度和更低的运营成本，使其更适合金融领域的实时应用。我们的研究结果强调了基于领域特定需求选择模型的重要性，并强调了定制专有模型在专门应用中相对于通用LLM的潜在优势。最终，我们选择实施专有的decoder-only模型来处理我们以前无法管理的复杂交易。该模型可以帮助我们提高14%的交易覆盖率，并节省超过1300万美元的年度成本。

## 🔬 方法详解

**问题定义**：论文旨在解决金融交易理解中，现有大型语言模型（LLM）在速度、成本和领域适应性方面的不足。现有方法，如直接使用或微调通用LLM，无法充分利用金融交易数据的特性，导致效率低下和性能瓶颈。

**核心思路**：论文的核心思路是构建专门针对金融交易数据的小规模专有模型。通过从头开始训练，模型可以更好地学习和适应金融领域的特定模式和语义，从而在速度和成本上优于通用LLM。

**技术框架**：论文评估了三种Transformer架构（Encoder-Only, Decoder-Only, Encoder-Decoder），并针对每种架构探索了三种训练方式（预训练LLM、微调LLM、从头训练的专有模型）。最终选择Decoder-Only架构，并从头训练专有模型。整体流程包括数据预处理、模型训练、评估和部署。

**关键创新**：最重要的技术创新在于针对金融交易数据定制化的小规模专有模型。与直接使用或微调通用LLM不同，该方法能够更好地利用领域知识，实现更高的效率和性能。

**关键设计**：论文最终选择并实现了一个专有的Decoder-Only模型。具体参数设置、损失函数和网络结构等技术细节未在摘要中详细说明，但强调了模型是根据金融交易数据的特性进行定制的。该模型最终提升了14%的交易覆盖率，并节省了超过1300万美元的年度成本。

## 📊 实验亮点

实验结果表明，定制化的小规模专有模型在金融交易理解任务中优于大型语言模型（如LLaMA3-8b、Flan-T5和SBERT）。该专有模型能够提高14%的交易覆盖率，并节省超过1300万美元的年度成本，突显了其在速度和成本效益方面的优势。

## 🎯 应用场景

该研究成果可应用于金融行业的多个领域，包括欺诈检测、合规性检查、风险评估和交易分析。通过提高金融交易理解的准确性和效率，可以降低运营成本，提升风险管理能力，并为决策提供更可靠的支持。未来，该方法可以推广到其他具有特定领域知识需求的场景。

## 📄 摘要（原文）

> Analyzing financial transactions is crucial for ensuring regulatory compliance, detecting fraud, and supporting decisions. The complexity of financial transaction data necessitates advanced techniques to extract meaningful insights and ensure accurate analysis. Since Transformer-based models have shown outstanding performance across multiple domains, this paper seeks to explore their potential in understanding financial transactions. This paper conducts extensive experiments to evaluate three types of Transformer models: Encoder-Only, Decoder-Only, and Encoder-Decoder models. For each type, we explore three options: pretrained LLMs, fine-tuned LLMs, and small proprietary models developed from scratch. Our analysis reveals that while LLMs, such as LLaMA3-8b, Flan-T5, and SBERT, demonstrate impressive capabilities in various natural language processing tasks, they do not significantly outperform small proprietary models in the specific context of financial transaction understanding. This phenomenon is particularly evident in terms of speed and cost efficiency. Proprietary models, tailored to the unique requirements of transaction data, exhibit faster processing times and lower operational costs, making them more suitable for real-time applications in the financial sector. Our findings highlight the importance of model selection based on domain-specific needs and underscore the potential advantages of customized proprietary models over general-purpose LLMs in specialized applications. Ultimately, we chose to implement a proprietary decoder-only model to handle the complex transactions that we previously couldn't manage. This model can help us to improve 14% transaction coverage, and save more than \$13 million annual cost.

