---
layout: default
title: "Pre-Forgettable Models: Prompt Learning as a Native Mechanism for Unlearning"
---

# Pre-Forgettable Models: Prompt Learning as a Native Mechanism for Unlearning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15230" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15230v1</a>
  <a href="https://arxiv.org/pdf/2509.15230.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15230v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15230v1', 'Pre-Forgettable Models: Prompt Learning as a Native Mechanism for Unlearning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rutger Hendrix, Giovanni Patanè, Leonardo G. Russo, Simone Carnemolla, Giovanni Bellitto, Federica Proietto Salanitri, Concetto Spampinato, Matteo Pennisi

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-05

**备注**: Accepted at ACM multimedia 2025 BNI track

**DOI**: [10.1145/3746027.3758171](https://doi.org/10.1145/3746027.3758171)

---

## 💡 一句话要点

**提出基于Prompt学习的预先可遗忘模型，实现高效、安全的知识移除。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可遗忘学习` `Prompt学习` `知识遗忘` `隐私保护` `深度学习`

## 📋 核心要点

1. 现有取消学习方法（如重训练）计算成本高，难以适应实时系统，无法满足隐私法规（如GDPR）对数据遗忘的需求。
2. 论文提出基于Prompt学习的预先可遗忘模型，将知识与Prompt Token绑定，通过移除Prompt实现知识遗忘，无需重训练。
3. 实验表明，该方法在保留剩余类别性能的同时，有效擦除目标类别知识，并具备抗成员推理攻击的隐私保护能力。

## 📝 摘要（中文）

基础模型已经通过在不同模态和任务中实现鲁棒且可迁移的表示，从而改变了多媒体分析。然而，它们的静态部署与日益增长的社会和监管需求相冲突——特别是根据GDPR等隐私框架的要求，需要应要求取消学习特定数据。传统的取消学习方法，包括重新训练、激活编辑或蒸馏，通常计算成本高昂、脆弱且不适合实时或不断发展的系统。在本文中，我们提出了一种范式转变：将取消学习重新思考为一种内置能力，而不是一种追溯干预。我们引入了一种基于prompt的学习框架，该框架在单个训练阶段统一了知识获取和移除。我们的方法不是将信息编码在模型权重中，而是将类级别的语义绑定到专用的prompt token。这种设计只需删除相应的prompt即可实现即时取消学习——无需重新训练、模型修改或访问原始数据。实验表明，我们的框架在保留类上的预测性能的同时，有效地擦除了被遗忘的类。除了实用性之外，我们的方法还表现出强大的隐私和安全保证：它能够抵抗成员推理攻击，并且prompt删除可以防止任何残留知识提取，即使在对抗条件下也是如此。这确保了符合数据保护原则，并防止未经授权访问被遗忘的信息，使该框架适合在敏感和受监管的环境中部署。总的来说，通过将可移除性嵌入到架构本身中，这项工作为设计模块化、可扩展和符合伦理的AI模型奠定了新的基础。

## 🔬 方法详解

**问题定义**：论文旨在解决基础模型在部署后难以高效、安全地遗忘特定数据的难题。现有取消学习方法，如重训练、激活编辑等，计算成本高昂，且可能影响模型在其他任务上的性能。此外，这些方法难以保证完全移除目标数据，存在隐私泄露风险。

**核心思路**：论文的核心思路是将知识的存储与模型的权重解耦，转而将类级别的语义信息绑定到特定的Prompt Token上。通过移除这些Prompt Token，即可实现对相应类别的知识遗忘，而无需修改模型的整体权重。这种方法将遗忘操作简化为Prompt的移除，从而实现高效且安全的知识遗忘。

**技术框架**：该框架主要包含以下几个阶段：1) Prompt Token初始化：为每个类别初始化一个或多个Prompt Token；2) Prompt学习：在训练过程中，模型学习将每个类别的语义信息编码到对应的Prompt Token中；3) 知识遗忘：通过移除与目标类别相关的Prompt Token，实现对该类别知识的遗忘；4) 模型推理：使用剩余的Prompt Token进行推理，模型仅能识别和预测未被遗忘的类别。

**关键创新**：该方法最重要的创新点在于将取消学习问题转化为Prompt Token的移除，从而避免了对模型权重的修改。这种方法不仅提高了遗忘效率，还降低了遗忘操作对模型性能的影响。此外，该方法还具备更强的隐私保护能力，能够有效抵抗成员推理攻击。

**关键设计**：论文的关键设计包括：1) Prompt Token的数量：每个类别分配的Prompt Token数量会影响模型的性能和遗忘效果；2) Prompt学习策略：如何有效地将类别的语义信息编码到Prompt Token中；3) 损失函数设计：如何平衡模型在保留类别上的性能和遗忘类别上的遗忘效果；4) 对抗攻击防御：设计相应的机制来防御针对Prompt Token的对抗攻击。

## 📊 实验亮点

实验结果表明，该方法在CIFAR-10和CIFAR-100数据集上，能够在有效遗忘目标类别的同时，保持模型在剩余类别上的预测准确率。此外，该方法还能够有效抵抗成员推理攻击，证明了其良好的隐私保护能力。与传统的重训练方法相比，该方法在遗忘效率上具有显著优势。

## 🎯 应用场景

该研究成果可应用于需要数据遗忘功能的各种场景，例如：1) 保护用户隐私，在用户要求删除个人数据时，快速且安全地移除模型中的相关信息；2) 应对法规要求，满足GDPR等隐私法规对数据遗忘的强制性要求；3) 模型更新与维护，在模型需要移除过时或错误知识时，高效地进行知识更新。

## 📄 摘要（原文）

> Foundation models have transformed multimedia analysis by enabling robust and transferable representations across diverse modalities and tasks. However, their static deployment conflicts with growing societal and regulatory demands -- particularly the need to unlearn specific data upon request, as mandated by privacy frameworks such as the GDPR. Traditional unlearning approaches, including retraining, activation editing, or distillation, are often computationally expensive, fragile, and ill-suited for real-time or continuously evolving systems. In this paper, we propose a paradigm shift: rethinking unlearning not as a retroactive intervention but as a built-in capability. We introduce a prompt-based learning framework that unifies knowledge acquisition and removal within a single training phase. Rather than encoding information in model weights, our approach binds class-level semantics to dedicated prompt tokens. This design enables instant unlearning simply by removing the corresponding prompt -- without retraining, model modification, or access to original data. Experiments demonstrate that our framework preserves predictive performance on retained classes while effectively erasing forgotten ones. Beyond utility, our method exhibits strong privacy and security guarantees: it is resistant to membership inference attacks, and prompt removal prevents any residual knowledge extraction, even under adversarial conditions. This ensures compliance with data protection principles and safeguards against unauthorized access to forgotten information, making the framework suitable for deployment in sensitive and regulated environments. Overall, by embedding removability into the architecture itself, this work establishes a new foundation for designing modular, scalable and ethically responsive AI models.

