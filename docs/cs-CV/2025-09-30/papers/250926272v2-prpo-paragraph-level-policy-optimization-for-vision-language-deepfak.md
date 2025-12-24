---
layout: default
title: "PRPO: Paragraph-level Policy Optimization for Vision-Language Deepfake Detection"
---

# PRPO: Paragraph-level Policy Optimization for Vision-Language Deepfake Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26272" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26272v2</a>
  <a href="https://arxiv.org/pdf/2509.26272.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26272v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26272v2', 'PRPO: Paragraph-level Policy Optimization for Vision-Language Deepfake Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tuan Nguyen, Naseem Khan, Khang Tran, NhatHai Phan, Issa Khalil

**分类**: cs.CV, cs.LG

**发布日期**: 2025-09-30 (更新: 2025-10-01)

---

## 💡 一句话要点

**提出PRPO算法，通过段落级策略优化提升视觉-语言大模型在Deepfake检测中的性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Deepfake检测` `多模态学习` `强化学习` `策略优化` `视觉-语言模型`

## 📋 核心要点

1. 现有Deepfake检测方法依赖大型数据集，但高质量数据集稀缺，限制了多模态大模型的推理能力。
2. PRPO算法通过段落级相对策略优化，将LLM的推理过程与图像内容在段落级别进行对齐。
3. 实验结果表明，PRPO显著提升了Deepfake检测的准确率，并在推理评分上取得了显著的提升。

## 📝 摘要（中文）

合成媒体的快速发展使得Deepfake检测成为在线安全和信任的关键挑战。然而，高质量大型数据集的稀缺限制了该领域的进展。尽管多模态大型语言模型（LLM）展现出强大的推理能力，但它们在Deepfake检测方面的表现不佳，常常产生与视觉证据不符或虚假的解释。为了解决这一局限性，我们引入了一个用于Deepfake检测的推理标注数据集，并提出了一种段落级相对策略优化（PRPO）的强化学习算法，该算法在段落级别将LLM推理与图像内容对齐。实验表明，PRPO显著提高了检测精度，并实现了最高的推理分数4.55/5.0。消融研究进一步表明，PRPO在测试时条件下明显优于GRPO。这些结果强调了将多模态推理建立在视觉证据基础上的重要性，从而实现更可靠和可解释的Deepfake检测。

## 🔬 方法详解

**问题定义**：现有方法在Deepfake检测中，多模态大语言模型虽然具备推理能力，但其推理结果往往与视觉证据不一致，甚至产生幻觉。缺乏高质量的推理标注数据集，使得模型难以有效学习视觉信息与文本推理之间的关联，导致检测精度不高。

**核心思路**：论文的核心思路是利用强化学习，通过段落级的策略优化，引导LLM生成与视觉内容对齐的推理过程。具体来说，就是奖励那些能够基于图像内容进行准确推理的段落，惩罚那些与图像内容不符或产生幻觉的段落。

**技术框架**：PRPO算法的技术框架主要包括以下几个部分：1) 一个用于Deepfake检测的推理标注数据集；2) 一个多模态大语言模型作为策略网络；3) 一个奖励函数，用于评估LLM生成的推理段落与图像内容的一致性；4) 一个强化学习算法，用于优化策略网络，使其生成更符合视觉证据的推理过程。

**关键创新**：PRPO的关键创新在于引入了段落级的相对策略优化。与传统的策略优化方法不同，PRPO不是直接优化整个推理过程，而是将推理过程分解为多个段落，并分别对每个段落进行优化。这种方法可以更精细地控制LLM的推理过程，使其更好地与视觉内容对齐。

**关键设计**：PRPO的关键设计包括：1) 使用相对奖励函数，鼓励生成更符合视觉证据的推理段落；2) 使用段落级的策略梯度更新，更精细地控制LLM的推理过程；3) 设计了专门的推理标注数据集，为强化学习提供高质量的训练数据。具体损失函数和网络结构细节未知。

## 📊 实验亮点

实验结果表明，PRPO算法在Deepfake检测精度上取得了显著提升，并且在推理评分上达到了4.55/5.0，表明该算法能够生成更符合视觉证据的推理过程。消融实验进一步证明，PRPO在测试时条件下优于GRPO，验证了段落级策略优化的有效性。

## 🎯 应用场景

该研究成果可应用于在线社交媒体平台、新闻媒体机构等，用于自动检测和识别Deepfake内容，从而减少虚假信息的传播，维护网络安全和公众信任。未来，该技术还可以扩展到其他多模态内容真实性检测领域，例如音频和视频篡改检测。

## 📄 摘要（原文）

> The rapid rise of synthetic media has made deepfake detection a critical challenge for online safety and trust. Progress remains constrained by the scarcity of large, high-quality datasets. Although multimodal large language models (LLMs) exhibit strong reasoning capabilities, their performance on deepfake detection is poor, often producing explanations that are misaligned with visual evidence or hallucinatory. To address this limitation, we introduce a reasoning-annotated dataset for deepfake detection and propose Paragraph-level Relative Policy Optimization (PRPO), a reinforcement learning algorithm that aligns LLM reasoning with image content at the paragraph level. Experiments show that PRPO improves detection accuracy by a wide margin and achieves the highest reasoning score of 4.55/5.0. Ablation studies further demonstrate that PRPO significantly outperforms GRPO under test-time conditions. These results underscore the importance of grounding multimodal reasoning in visual evidence to enable more reliable and interpretable deepfake detection.

