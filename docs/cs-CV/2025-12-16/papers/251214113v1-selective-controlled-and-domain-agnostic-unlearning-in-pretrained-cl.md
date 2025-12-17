---
layout: default
title: Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach
---

# Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach

**arXiv**: [2512.14113v1](https://arxiv.org/abs/2512.14113) | [PDF](https://arxiv.org/pdf/2512.14113.pdf)

**作者**: Ashish Mishra, Gyanaranjan Nayak, Tarun Kumar, Arpit Shah, Suparna Bhattacharya, Martin Foltin

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出一种无需训练和数据的CLIP选择性遗忘框架，实现跨域、领域特定和选择性领域的可控知识移除。**

🎯 **匹配领域**: **强化学习**

**关键词**: `CLIP模型` `知识遗忘` `多模态学习` `零样本分类` `嵌入空间优化` `无需训练方法` `可控遗忘` `视觉域适应`

## 📋 核心要点

1. 核心问题：现有遗忘方法通常依赖重新训练或额外数据，计算成本高且灵活性不足，难以实现跨域或领域特定的选择性知识移除。
2. 方法要点：提出一种无需训练和数据的框架，通过多模态零空间整合文本提示和合成视觉原型，实现三种遗忘范式，高效移除目标类别信息。
3. 实验或效果：在多种视觉域上验证，该方法能有效移除指定知识，同时保持模型在其他任务上的性能，相比基线方法计算效率更高。

## 📝 摘要（中文）

预训练模型如CLIP在多种视觉领域（如自然图像、艺术渲染和抽象表示）中展现出卓越的零样本分类能力。然而，实际应用常需移除特定对象类别的知识（即“遗忘”），且要求无需额外数据或重新训练，同时不影响模型在无关任务上的性能。本文提出一种新颖的无需训练和数据的遗忘框架，支持三种遗忘范式：（1）在所有域中全局遗忘选定对象，（2）领域特定知识移除（例如，消除草图表示同时保留照片识别），以及（3）在选择性域中完全遗忘。通过利用多模态零空间，结合文本提示和从CLIP联合嵌入空间衍生的合成视觉原型，该方法高效移除不需要的类别信息，同时保留其余知识。此方法克服了现有基于重新训练方法的局限性，为可控模型遗忘提供了灵活且计算高效的解决方案。

## 🔬 方法详解

整体框架基于CLIP的预训练模型，无需额外训练或数据。关键技术创新点在于利用多模态零空间，通过协同整合文本提示和从CLIP联合嵌入空间合成的视觉原型，构建遗忘机制。具体地，通过优化嵌入空间中的表示，使目标类别的信息被抑制或消除，同时最小化对其他类别的影响。与现有方法的主要区别在于：本方法完全避免重新训练，支持跨域和领域特定的选择性遗忘，且操作在嵌入空间层面，计算效率更高，灵活性更强。

## 📊 实验亮点

实验表明，该方法在多种视觉域（如照片、草图）上成功实现选择性遗忘，移除目标类别后模型在其他任务上的性能下降最小，相比重新训练方法节省大量计算资源，验证了其高效性和可控性。

## 🎯 应用场景

该研究可应用于隐私保护（如移除敏感类别）、模型合规性调整（如删除侵权内容）和多模态系统优化（如定制化知识库），为AI模型提供可控遗忘能力，提升实际部署的适应性和安全性。

## 📄 摘要（原文）

> Pretrained models like CLIP have demonstrated impressive zero-shot classification capabilities across diverse visual domains, spanning natural images, artistic renderings, and abstract representations. However, real-world applications often demand the removal (or "unlearning") of specific object classes without requiring additional data or retraining, or affecting the model's performance on unrelated tasks. In this paper, we propose a novel training- and data-free unlearning framework that enables three distinct forgetting paradigms: (1) global unlearning of selected objects across all domains, (2) domain-specific knowledge removal (e.g., eliminating sketch representations while preserving photo recognition), and (3) complete unlearning in selective domains. By leveraging a multimodal nullspace through synergistic integration of text prompts and synthesized visual prototypes derived from CLIP's joint embedding space, our method efficiently removes undesired class information while preserving the remaining knowledge. This approach overcomes the limitations of existing retraining-based methods and offers a flexible and computationally efficient solution for controlled model forgetting.

