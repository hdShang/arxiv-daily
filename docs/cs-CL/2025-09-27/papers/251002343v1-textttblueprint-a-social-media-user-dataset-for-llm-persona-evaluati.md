---
layout: default
title: "$\\texttt{BluePrint}$: A Social Media User Dataset for LLM Persona Evaluation and Training"
---

# $\texttt{BluePrint}$: A Social Media User Dataset for LLM Persona Evaluation and Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02343" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02343v1</a>
  <a href="https://arxiv.org/pdf/2510.02343.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02343v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02343v1', '$\texttt{BluePrint}$: A Social Media User Dataset for LLM Persona Evaluation and Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aurélien Bück-Kaeffer, Je Qin Chooi, Dan Zhao, Maximilian Puelma Touzel, Kellin Pelrine, Jean-François Godbout, Reihaneh Rabbany, Zachary Yang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-27

**备注**: 8 pages, 4 figures, 11 tables

---

## 💡 一句话要点

**提出BluePrint数据集，用于评估和训练LLM在社交媒体中的用户行为模拟。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社交媒体模拟` `大型语言模型` `用户行为建模` `数据集构建` `隐私保护`

## 📋 核心要点

1. 现有方法缺乏标准化的社交媒体数据集，难以有效训练和评估LLM在模拟用户行为方面的能力。
2. 论文提出SIMPACT框架，通过尊重隐私的方式构建行为导向的社交媒体数据集，用于训练和评估LLM代理。
3. 发布BluePrint数据集，该数据集基于Bluesky的政治讨论数据，包含用户行为角色和社交互动动作，可作为评估基准。

## 📝 摘要（中文）

大型语言模型（LLMs）在模拟大规模社交媒体动态方面展现出潜力，为伦理或后勤上难以通过人类受试者进行的研究提供了可能。然而，该领域缺乏标准化的数据资源，用于微调和评估LLM作为逼真的社交媒体代理。为了解决这一问题，我们引入了SIMPACT，即面向模拟的Persona和Action Capture Toolkit，这是一个尊重隐私的框架，用于构建适合训练代理模型的、基于行为的社交媒体数据集。我们将下一个动作预测定义为训练和评估基于LLM的代理的任务，并引入了集群和群体层面的指标，以评估行为保真度和风格真实性。作为一个具体的实现，我们发布了BluePrint，这是一个基于公共Bluesky数据构建的大规模数据集，专注于政治讨论。BluePrint将匿名用户聚类成聚合行为的角色，在通过假名化和删除个人身份信息来保护隐私的同时，捕捉真实的参与模式。该数据集包括一个包含12种社交媒体互动类型（点赞、回复、转发等）的大型动作集，每个实例都与之前的发布活动相关联。这支持了代理的开发，这些代理不仅在语言上，而且在社交媒体的互动行为中使用上下文依赖性来建模社交媒体用户。通过标准化数据和评估协议，SIMPACT为推进严谨、符合伦理的社交媒体模拟奠定了基础。BluePrint既可以作为政治讨论建模的评估基准，也可以作为构建特定领域数据集以研究诸如错误信息和两极分化等挑战的模板。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在模拟社交媒体用户行为时，缺乏高质量、标准化的数据集进行训练和评估。现有的数据集要么规模不足，要么缺乏对用户行为的细粒度建模，难以保证模拟的真实性和有效性。此外，隐私保护也是一个重要的挑战，直接使用用户数据可能导致隐私泄露。

**核心思路**：论文的核心思路是构建一个既能反映真实社交媒体用户行为，又能保护用户隐私的数据集。通过将用户聚类成不同的角色（persona），并捕捉每个角色的行为模式，可以在不暴露个体用户身份信息的情况下，模拟社交媒体的动态。同时，将下一个动作预测作为训练和评估LLM代理的任务，可以有效地衡量模型对用户行为的理解和预测能力。

**技术框架**：论文提出了SIMPACT框架，用于构建社交媒体数据集。该框架包含以下几个主要步骤：1) 数据收集：从公共社交媒体平台收集数据，例如Bluesky。2) 用户聚类：将用户聚类成不同的角色（persona），每个角色代表一组具有相似行为模式的用户。3) 行为建模：捕捉每个角色的社交互动行为，例如点赞、回复、转发等。4) 数据集构建：将用户角色和行为数据组合成一个数据集，用于训练和评估LLM代理。5) 隐私保护：通过假名化和删除个人身份信息来保护用户隐私。

**关键创新**：论文的关键创新在于提出了SIMPACT框架，该框架能够以一种尊重隐私的方式构建高质量的社交媒体数据集。与现有方法相比，SIMPACT框架更加注重对用户行为的细粒度建模，能够捕捉到用户在社交媒体上的真实互动模式。此外，论文还提出了新的评估指标，用于衡量LLM代理在行为保真度和风格真实性方面的表现。

**关键设计**：BluePrint数据集包含12种社交媒体互动类型（点赞、回复、转发等），每个实例都与之前的发布活动相关联。用户被聚类成不同的角色，每个角色代表一组具有相似行为模式的用户。数据集的构建过程中，采用了假名化和删除个人身份信息等技术来保护用户隐私。论文还提出了集群层面和群体层面的评估指标，用于衡量LLM代理在行为保真度和风格真实性方面的表现。具体参数设置和损失函数等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

论文发布了BluePrint数据集，该数据集基于Bluesky的政治讨论数据，包含大量用户行为数据和社交互动信息。该数据集可以作为评估LLM代理在模拟社交媒体用户行为方面的基准。论文还提出了新的评估指标，用于衡量LLM代理在行为保真度和风格真实性方面的表现。具体的性能数据和对比基线在摘要中未提及，属于未知信息。

## 🎯 应用场景

该研究成果可应用于社交媒体行为预测、舆情分析、虚假信息检测等领域。通过训练LLM代理模拟社交媒体用户行为，可以更好地理解社交媒体的动态，预测用户行为，并采取相应的措施来应对虚假信息和网络暴力等问题。此外，该研究还可以为社交媒体平台提供更好的用户推荐和内容推荐服务。

## 📄 摘要（原文）

> Large language models (LLMs) offer promising capabilities for simulating social media dynamics at scale, enabling studies that would be ethically or logistically challenging with human subjects. However, the field lacks standardized data resources for fine-tuning and evaluating LLMs as realistic social media agents. We address this gap by introducing SIMPACT, the SIMulation-oriented Persona and Action Capture Toolkit, a privacy respecting framework for constructing behaviorally-grounded social media datasets suitable for training agent models. We formulate next-action prediction as a task for training and evaluating LLM-based agents and introduce metrics at both the cluster and population levels to assess behavioral fidelity and stylistic realism. As a concrete implementation, we release BluePrint, a large-scale dataset built from public Bluesky data focused on political discourse. BluePrint clusters anonymized users into personas of aggregated behaviours, capturing authentic engagement patterns while safeguarding privacy through pseudonymization and removal of personally identifiable information. The dataset includes a sizable action set of 12 social media interaction types (likes, replies, reposts, etc.), each instance tied to the posting activity preceding it. This supports the development of agents that use context-dependence, not only in the language, but also in the interaction behaviours of social media to model social media users. By standardizing data and evaluation protocols, SIMPACT provides a foundation for advancing rigorous, ethically responsible social media simulations. BluePrint serves as both an evaluation benchmark for political discourse modeling and a template for building domain specific datasets to study challenges such as misinformation and polarization.

