---
layout: default
title: "Improving LLM Safety and Helpfulness using SFT and DPO: A Study on OPT-350M"
---

# Improving LLM Safety and Helpfulness using SFT and DPO: A Study on OPT-350M

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09055" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09055v1</a>
  <a href="https://arxiv.org/pdf/2509.09055.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09055v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09055v1', 'Improving LLM Safety and Helpfulness using SFT and DPO: A Study on OPT-350M')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Piyush Pant

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-10

**备注**: 17 pages, 3 figures. Code and dataset available at https://github.com/PiyushWithPant/Improving-LLM-Safety-and-Helpfulness-using-SFT-and-DPO

---

## 💡 一句话要点

**SFT与DPO结合提升OPT-350M安全性与有用性：一种综合对齐策略研究**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `语言模型对齐` `监督微调` `直接偏好优化` `安全性` `有用性` `OPT-350M` `RLHF数据集`

## 📋 核心要点

1. 现有方法难以兼顾语言模型的安全性与有用性，尤其是在资源受限的模型上。
2. 论文提出结合监督微调（SFT）和直接偏好优化（DPO）的策略，以实现更优的模型对齐。
3. 实验表明，SFT+DPO模型在无害率、有用率和综合对齐得分上均优于单独使用SFT或DPO的模型。

## 📝 摘要（中文）

本研究探讨了对齐技术，即监督微调（SFT）、直接偏好优化（DPO）以及SFT+DPO组合方法，在提升OPT-350M语言模型的安全性和有用性方面的有效性。我们利用Anthropic Helpful-Harmless RLHF数据集训练并评估了四个模型：基础OPT350M模型、SFT模型、DPO模型以及SFT+DPO模型。我们引入了三个关键评估指标：无害率（HmR）、有用率（HpR）和综合对齐得分（CAS），所有这些指标均来自奖励模型输出。结果表明，虽然SFT优于DPO，但SFT+DPO模型在所有指标上均优于其他模型，证明了这些技术的互补性。我们的研究结果还强调了噪声数据、有限的GPU资源和训练约束所带来的挑战。本研究全面展示了微调策略如何影响模型对齐，并为未来更强大的对齐管道奠定了基础。

## 🔬 方法详解

**问题定义**：论文旨在解决如何有效提升小型语言模型（OPT-350M）的安全性和有用性，现有方法如单独使用SFT或DPO可能无法达到最佳效果，且在资源有限的情况下训练对齐模型面临挑战。

**核心思路**：核心思路是将监督微调（SFT）和直接偏好优化（DPO）相结合，利用SFT快速学习任务，DPO则基于人类偏好进行优化，从而互补两种方法的优势，实现更好的模型对齐。

**技术框架**：整体流程包括：1）使用Anthropic Helpful-Harmless RLHF数据集；2）训练四个模型：基础OPT350M、SFT模型、DPO模型和SFT+DPO模型；3）使用奖励模型评估模型的无害率（HmR）、有用率（HpR）和综合对齐得分（CAS）。

**关键创新**：关键创新在于发现SFT和DPO的互补性，并证明将两者结合使用可以显著提升模型的安全性和有用性，优于单独使用任何一种方法。此外，论文还针对小型模型和有限资源环境进行了优化。

**关键设计**：论文使用了Anthropic Helpful-Harmless RLHF数据集进行训练，该数据集包含人类对模型输出的偏好信息。SFT使用标准交叉熵损失函数，DPO使用标准的DPO损失函数。SFT+DPO模型先进行SFT训练，然后再进行DPO训练。评估指标包括无害率（HmR）、有用率（HpR）和综合对齐得分（CAS），这些指标基于奖励模型输出计算得出。

## 📊 实验亮点

实验结果表明，SFT+DPO模型在所有评估指标上均优于其他模型。具体而言，SFT+DPO模型在无害率（HmR）、有用率（HpR）和综合对齐得分（CAS）上均取得了显著提升，证明了SFT和DPO的互补性。虽然SFT单独训练效果优于DPO，但SFT+DPO的组合策略实现了最佳性能。

## 🎯 应用场景

该研究成果可应用于各种需要安全和有用的语言模型的场景，例如智能客服、内容生成、教育辅助等。通过结合SFT和DPO，可以训练出更加符合人类价值观和需求的语言模型，从而提升用户体验并降低潜在风险。该方法尤其适用于资源受限的场景，为小型语言模型的对齐提供了一种有效的解决方案。

## 📄 摘要（原文）

> This research investigates the effectiveness of alignment techniques, Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and a combined SFT+DPO approach on improving the safety and helpfulness of the OPT-350M language model. Utilizing the Anthropic Helpful-Harmless RLHF dataset, we train and evaluate four models: the base OPT350M, an SFT model, a DPO model, and a model trained with both SFT and DPO. We introduce three key evaluation metrics: Harmlessness Rate (HmR), Helpfulness Rate (HpR), and a Combined Alignment Score (CAS), all derived from reward model outputs. The results show that while SFT outperforms DPO, The combined SFT+DPO model outperforms all others across all metrics, demonstrating the complementary nature of these techniques. Our findings also highlight challenges posed by noisy data, limited GPU resources, and training constraints. This study offers a comprehensive view of how fine-tuning strategies affect model alignment and provides a foundation for more robust alignment pipelines in future work.

