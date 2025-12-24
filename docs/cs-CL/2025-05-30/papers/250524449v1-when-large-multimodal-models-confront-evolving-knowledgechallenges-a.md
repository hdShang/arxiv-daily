---
layout: default
title: When Large Multimodal Models Confront Evolving Knowledge:Challenges and Pathways
---

# When Large Multimodal Models Confront Evolving Knowledge:Challenges and Pathways

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24449" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24449v1</a>
  <a href="https://arxiv.org/pdf/2505.24449.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24449v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24449v1', 'When Large Multimodal Models Confront Evolving Knowledge:Challenges and Pathways')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kailin Jiang, Yuntao Du, Yukai Ding, Yuchen Ren, Ning Jiang, Zhi Gao, Zilong Zheng, Lei Liu, Bin Li, Qing Li

**分类**: cs.CL

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出EVOKE基准以解决多模态模型知识演变问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `知识注入` `演变知识` `持续学习` `灾难性遗忘` `EVOKE基准` `文本增强` `图像增强`

## 📋 核心要点

1. 现有知识注入方法在处理演变知识时表现不佳，导致模型无法有效更新其知识库。
2. 提出EVOKE基准，旨在评估多模态模型在现实场景中注入演变知识的能力，并探索有效的知识注入方法。
3. 实验结果表明，文本知识增强能显著提升模型性能，而持续学习方法有效减轻了灾难性遗忘现象。

## 📝 摘要（中文）

大型语言/多模态模型（LLMs/LMMs）存储了大量预训练知识，但在与现实世界更新保持一致性方面面临挑战，尤其是在获取演变知识时容易出现灾难性遗忘。以往研究主要集中于构建文本知识数据集和探索知识注入，缺乏对多模态演变知识注入的探讨。为此，本文提出了EVOKE基准，以评估LMMs在现实场景中注入多模态演变知识的能力。研究发现现有知识注入方法在演变知识上表现不佳，且监督微调会导致灾难性遗忘，特别是指令跟随能力受到严重影响。我们还发现文本知识增强在训练阶段能提升性能，而图像增强效果不佳，持续学习方法如Replay和MoELoRA能有效减轻遗忘。

## 🔬 方法详解

**问题定义**：本文旨在解决大型多模态模型在面对演变知识时的知识注入不足问题。现有方法在演变知识的处理上表现不佳，导致模型无法有效更新和保持知识一致性。

**核心思路**：提出EVOKE基准，以评估多模态模型在现实场景中注入演变知识的能力，并探索文本和图像知识增强的效果。通过引入持续学习方法，减轻模型的灾难性遗忘。

**技术框架**：整体架构包括知识注入模块、评估模块和持续学习模块。知识注入模块负责将演变知识注入模型，评估模块用于测试模型在新知识上的表现，持续学习模块则应用Replay和MoELoRA等方法来减轻遗忘。

**关键创新**：最重要的创新在于提出了EVOKE基准，专注于多模态演变知识的注入评估，填补了现有研究的空白。与传统的知识注入方法相比，本文强调了持续学习的重要性。

**关键设计**：在参数设置上，采用了文本知识增强策略，而图像增强未能显著提升性能。损失函数设计上，结合了传统的监督学习损失与持续学习损失，以平衡新旧知识的学习。

## 📊 实验亮点

实验结果显示，文本知识增强在训练阶段显著提升了模型性能，而图像增强未能取得相同效果。持续学习方法如Replay和MoELoRA有效减轻了灾难性遗忘，提升了模型在新知识上的表现，表明当前知识注入方法在演变知识处理上存在显著局限性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶、医疗影像分析等多模态系统，能够帮助这些系统在动态环境中保持知识的更新与一致性。未来，随着知识注入方法的进一步优化，模型的智能化水平将显著提升，推动更多实际应用的发展。

## 📄 摘要（原文）

> Large language/multimodal models (LLMs/LMMs) store extensive pre-trained knowledge but struggle to maintain consistency with real-world updates, making it difficult to avoid catastrophic forgetting while acquiring evolving knowledge. Previous work focused on constructing textual knowledge datasets and exploring knowledge injection in LLMs, lacking exploration of multimodal evolving knowledge injection in LMMs. To address this, we propose the EVOKE benchmark to evaluate LMMs' ability to inject multimodal evolving knowledge in real-world scenarios. Meanwhile, a comprehensive evaluation of multimodal evolving knowledge injection revealed two challenges: (1) Existing knowledge injection methods perform terribly on evolving knowledge. (2) Supervised fine-tuning causes catastrophic forgetting, particularly instruction following ability is severely compromised. Additionally, we provide pathways and find that: (1) Text knowledge augmentation during the training phase improves performance, while image augmentation cannot achieve it. (2) Continual learning methods, especially Replay and MoELoRA, effectively mitigate forgetting. Our findings indicate that current knowledge injection methods have many limitations on evolving knowledge, which motivates further research on more efficient and stable knowledge injection methods.

