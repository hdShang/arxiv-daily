---
layout: default
title: PA-FAS: Towards Interpretable and Generalizable Multimodal Face Anti-Spoofing via Path-Augmented Reinforcement Learning
---

# PA-FAS: Towards Interpretable and Generalizable Multimodal Face Anti-Spoofing via Path-Augmented Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.17927" class="toolbar-btn" target="_blank">📄 arXiv: 2511.17927v1</a>
  <a href="https://arxiv.org/pdf/2511.17927.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.17927v1" onclick="toggleFavorite(this, '2511.17927v1', 'PA-FAS: Towards Interpretable and Generalizable Multimodal Face Anti-Spoofing via Path-Augmented Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingjie Ma, Xun Lin, Yong Xu, Weicheng Xie, Zitong Yu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-22

**备注**: Accepted by AAAI 2026 (Oral)

---

## 💡 一句话要点

**提出PA-FAS，通过路径增强强化学习提升多模态人脸反欺骗的泛化性和可解释性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人脸反欺骗` `多模态融合` `强化学习` `路径增强` `跨域泛化`

## 📋 核心要点

1. 现有方法在多模态人脸反欺骗中，面临推理路径受限和单任务监督与多样推理路径不匹配的问题，导致泛化性和可解释性不足。
2. PA-FAS通过构建高质量的扩展推理序列来增强推理路径，并引入答案洗牌机制，避免模型利用捷径，从而提升推理深度。
3. 实验结果表明，PA-FAS显著提高了多模态推理的准确性和跨域泛化能力，实现了更可信赖的人脸反欺骗。

## 📝 摘要（中文）

人脸反欺骗(FAS)近年来在多模态融合、跨域泛化和可解释性方面取得了进展。借助大型语言模型和强化学习(RL)，基于策略的训练为联合建模这些方面提供了新的机会。然而，多模态推理比单模态推理更复杂，需要准确的特征表示和跨模态验证，同时面临高质量标注数据稀缺的问题，这使得直接应用RL效果欠佳。我们发现监督微调加RL(SFT+RL)用于多模态FAS存在两个关键限制：(1)有限的多模态推理路径限制了互补模态的使用，并缩小了SFT后的探索空间，削弱了RL的效果；(2)单任务监督与多样化推理路径不匹配导致推理混淆，模型可能利用捷径将图像直接映射到答案，而忽略了预期的推理。为了解决这个问题，我们提出了PA-FAS，它通过从有限的标注中构建高质量的扩展推理序列来增强推理路径，丰富路径并放松探索约束。我们进一步在SFT期间引入了一种答案洗牌机制，以强制进行全面的多模态分析，而不是使用表面线索，从而鼓励更深入的推理并减轻捷径学习。PA-FAS显著提高了多模态推理的准确性和跨域泛化能力，并更好地统一了多模态融合、泛化和可解释性，从而实现可信赖的FAS。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态人脸反欺骗任务中，现有方法由于推理路径受限和监督方式不当导致的泛化能力差和可解释性低的问题。现有方法通常采用监督微调加强化学习(SFT+RL)的框架，但存在两个痛点：一是多模态推理路径有限，无法充分利用不同模态的互补信息；二是单任务监督容易导致模型学习捷径，忽略深层推理过程。

**核心思路**：论文的核心思路是通过增强推理路径和改进监督方式来提升模型的推理能力和泛化能力。具体来说，通过构建高质量的扩展推理序列来丰富推理路径，并采用答案洗牌机制来避免模型学习捷径，从而鼓励模型进行更深入的多模态分析。

**技术框架**：PA-FAS的整体框架包括两个主要阶段：首先是监督微调(SFT)阶段，该阶段使用答案洗牌机制来训练模型，避免模型学习捷径。然后是强化学习(RL)阶段，该阶段使用增强的推理路径来训练模型，鼓励模型进行更深入的多模态分析。

**关键创新**：论文的关键创新在于提出了路径增强和答案洗牌两种机制。路径增强通过构建高质量的扩展推理序列来丰富推理路径，从而提升模型的推理能力。答案洗牌通过随机打乱答案的顺序来避免模型学习捷径，从而鼓励模型进行更深入的多模态分析。

**关键设计**：在SFT阶段，答案洗牌机制通过随机打乱训练样本的答案顺序，迫使模型不能简单地将图像映射到答案，而是需要进行更深入的多模态分析。在RL阶段，路径增强通过构建高质量的扩展推理序列，为模型提供更多的探索空间，从而提升模型的推理能力。具体的损失函数和网络结构细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

PA-FAS在多个人脸反欺骗数据集上取得了显著的性能提升。实验结果表明，PA-FAS不仅提高了多模态推理的准确性，还显著提升了跨域泛化能力。具体的性能数据和对比基线在论文中进行了详细描述（未知）。

## 🎯 应用场景

该研究成果可应用于身份验证、访问控制、金融安全等领域，有效防御基于人脸欺骗的攻击，提升系统的安全性与可靠性。未来，该方法有望扩展到更多模态和更复杂的反欺骗场景，例如语音反欺骗、行为反欺骗等，具有广阔的应用前景。

## 📄 摘要（原文）

> Face anti-spoofing (FAS) has recently advanced in multimodal fusion, cross-domain generalization, and interpretability. With large language models and reinforcement learning (RL), strategy-based training offers new opportunities to jointly model these aspects. However, multimodal reasoning is more complex than unimodal reasoning, requiring accurate feature representation and cross-modal verification while facing scarce, high-quality annotations, which makes direct application of RL sub-optimal. We identify two key limitations of supervised fine-tuning plus RL (SFT+RL) for multimodal FAS: (1) limited multimodal reasoning paths restrict the use of complementary modalities and shrink the exploration space after SFT, weakening the effect of RL; and (2) mismatched single-task supervision versus diverse reasoning paths causes reasoning confusion, where models may exploit shortcuts by mapping images directly to answers and ignoring the intended reasoning. To address this, we propose PA-FAS, which enhances reasoning paths by constructing high-quality extended reasoning sequences from limited annotations, enriching paths and relaxing exploration constraints. We further introduce an answer-shuffling mechanism during SFT to force comprehensive multimodal analysis instead of using superficial cues, thereby encouraging deeper reasoning and mitigating shortcut learning. PA-FAS significantly improves multimodal reasoning accuracy and cross-domain generalization, and better unifies multimodal fusion, generalization, and interpretability for trustworthy FAS.

