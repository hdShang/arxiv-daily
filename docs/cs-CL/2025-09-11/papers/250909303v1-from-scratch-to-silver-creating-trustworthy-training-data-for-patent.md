---
layout: default
title: "From scratch to silver: Creating trustworthy training data for patent-SDG classification using Large Language Models"
---

# From scratch to silver: Creating trustworthy training data for patent-SDG classification using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09303" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09303v1</a>
  <a href="https://arxiv.org/pdf/2509.09303.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09303v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09303v1', 'From scratch to silver: Creating trustworthy training data for patent-SDG classification using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Grazia Sveva Ascione, Nicolò Tamagnone

**分类**: cs.CL

**发布日期**: 2025-09-11

---

## 💡 一句话要点

**利用大型语言模型创建可信的专利-SDG分类训练数据，解决标注数据稀缺问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `专利分类` `可持续发展目标` `大型语言模型` `弱监督学习` `银标准数据集`

## 📋 核心要点

1. 现有专利-SDG分类方法依赖关键词或引用，缺乏可扩展性和泛化性，难以有效追踪创新对全球挑战的贡献。
2. 论文提出一种基于大型语言模型的弱监督方法，从专利和SDG论文中提取结构化概念，构建复合标注函数。
3. 实验表明，该方法在内部和外部验证中均优于现有基线方法，能够生成更具主题一致性的专利分类。

## 📝 摘要（中文）

本研究旨在解决专利与联合国可持续发展目标（SDGs）分类中缺乏大规模标注数据集的问题。现有方法如关键词搜索、迁移学习和基于引用的启发式方法，在可扩展性和泛化性方面存在局限。本文将专利-SDG分类视为弱监督问题，利用专利对SDG相关科学出版物的引用（NPL引用）作为初始噪声信号。为了解决其稀疏性和噪声问题，我们开发了一种复合标注函数（LF），该函数使用大型语言模型（LLM）从专利和SDG论文中提取结构化概念，即功能、解决方案和应用，并基于专利本体计算跨域相似度，然后使用基于排序的检索方法进行组合。通过自定义的正样本损失函数校准LF，使其与已知的NPL-SDG链接对齐，而不惩罚新SDG关联的发现。最终生成一个银标准、软多标签数据集，将专利映射到SDGs，从而能够训练有效的多标签回归模型。通过内部验证和外部验证，验证了该方法的有效性。

## 🔬 方法详解

**问题定义**：专利与联合国可持续发展目标（SDGs）的分类对于追踪创新如何应对全球挑战至关重要。然而，缺乏大规模标注数据集限制了监督学习的应用。现有方法，如关键词搜索、迁移学习和基于引用的启发式方法，存在可扩展性和泛化性问题，无法有效利用海量专利数据。

**核心思路**：论文的核心思路是将专利-SDG分类问题转化为一个弱监督问题，利用专利对SDG相关科学出版物的引用（NPL引用）作为初始的噪声标签。通过大型语言模型（LLM）提取专利和SDG论文中的语义信息，构建更鲁棒的标注函数，从而生成高质量的银标准训练数据。

**技术框架**：整体框架包含以下几个主要阶段：1) 利用NPL引用构建初始弱标签；2) 使用LLM从专利和SDG论文中提取结构化概念（功能、解决方案、应用）；3) 计算专利和SDG论文之间的跨域相似度；4) 使用基于排序的检索方法组合相似度得分；5) 通过自定义的正样本损失函数校准标注函数，生成银标准数据集；6) 使用银标准数据集训练多标签回归模型。

**关键创新**：最重要的技术创新点在于利用大型语言模型提取专利和SDG论文中的结构化语义信息，并将其融入到标注函数中。与传统的基于关键词或引用的方法相比，该方法能够更准确地捕捉专利与SDG之间的关联，并有效降低噪声标签的影响。此外，自定义的正样本损失函数能够更好地利用已知的NPL-SDG链接，同时允许发现新的SDG关联。

**关键设计**：论文使用了一种复合标注函数，该函数结合了多个相似度得分，包括基于功能、解决方案和应用的相似度。这些相似度得分通过基于排序的检索方法进行组合，以提高检索的准确性。此外，论文还设计了一个自定义的正样本损失函数，该函数只惩罚与已知NPL-SDG链接不一致的预测，而不惩罚发现新的SDG关联。具体的LLM选择和参数设置在论文中有详细描述。

## 📊 实验亮点

实验结果表明，该方法在内部验证中优于基于Transformer的模型和零样本LLM，在外部验证中，使用该方法生成的标签在专利引用、共同发明人和共同申请人网络中表现出比传统技术分类更高的主题、认知和组织一致性。具体性能数据和提升幅度在论文中有详细展示。

## 🎯 应用场景

该研究成果可应用于大规模专利数据的SDG分类，帮助政府、企业和研究机构更好地了解创新对可持续发展目标的贡献。此外，该方法生成的银标准数据集可用于训练更有效的专利分析模型，为技术趋势预测、竞争情报分析等提供支持。未来，该方法可以扩展到其他领域，例如科技文献分类、政策文本分析等。

## 📄 摘要（原文）

> Classifying patents by their relevance to the UN Sustainable Development Goals (SDGs) is crucial for tracking how innovation addresses global challenges. However, the absence of a large, labeled dataset limits the use of supervised learning. Existing methods, such as keyword searches, transfer learning, and citation-based heuristics, lack scalability and generalizability. This paper frames patent-to-SDG classification as a weak supervision problem, using citations from patents to SDG-tagged scientific publications (NPL citations) as a noisy initial signal. To address its sparsity and noise, we develop a composite labeling function (LF) that uses large language models (LLMs) to extract structured concepts, namely functions, solutions, and applications, from patents and SDG papers based on a patent ontology. Cross-domain similarity scores are computed and combined using a rank-based retrieval approach. The LF is calibrated via a custom positive-only loss that aligns with known NPL-SDG links without penalizing discovery of new SDG associations. The result is a silver-standard, soft multi-label dataset mapping patents to SDGs, enabling the training of effective multi-label regression models. We validate our approach through two complementary strategies: (1) internal validation against held-out NPL-based labels, where our method outperforms several baselines including transformer-based models, and zero-shot LLM; and (2) external validation using network modularity in patent citation, co-inventor, and co-applicant graphs, where our labels reveal greater thematic, cognitive, and organizational coherence than traditional technological classifications. These results show that weak supervision and semantic alignment can enhance SDG classification at scale.

