---
layout: default
title: VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation
---

# VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23497" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23497v2</a>
  <a href="https://arxiv.org/pdf/2510.23497.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23497v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.23497v2', 'VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Walid Bousselham, Hilde Kuehne, Cordelia Schmid

**分类**: cs.CV

**发布日期**: 2025-10-27 (更新: 2025-10-28)

**备注**: www.walidbousselham.com/VOLD/

---

## 💡 一句话要点

**提出VOLD框架，通过策略蒸馏将LLM的推理能力迁移到视觉-语言模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉-语言模型` `推理能力迁移` `在线策略蒸馏` `强化学习` `群体相对策略优化`

## 📋 核心要点

1. VLM在复杂推理任务中面临数据稀缺的挑战，限制了其性能提升。
2. VOLD框架通过在线策略蒸馏，将文本LLM的推理能力迁移到VLM，实现知识共享。
3. 实验表明，VOLD在多个推理基准上显著优于现有方法，验证了其有效性。

## 📝 摘要（中文）

针对视觉-语言模型(VLM)在复杂推理方面面临的挑战，特别是高质量图像-文本推理数据稀缺的问题，本文提出了VOLD框架，旨在将纯文本教师模型的推理能力迁移到VLM学生模型。VOLD结合了基于群体相对策略优化(GRPO)的强化学习和在线策略蒸馏，利用教师模型的推理轨迹来指导学生模型，从而显著优于单独使用GRPO。研究表明，冷启动对齐对于在线训练阶段的有效迁移至关重要，如果教师和学生之间的分布对齐不足，在线策略蒸馏将无法提供有意义的指导。VOLD在MMMU-Pro、MathVision、MathVista和LogicVista等多个基准测试中进行了评估，结果表明VOLD显著优于基线模型，并在现有技术水平上有所提高。消融实验表明，通过SFT进行冷启动对齐对于使用纯文本教师模型的在线策略蒸馏至关重要。

## 🔬 方法详解

**问题定义**：视觉-语言模型(VLM)在进行复杂推理时，面临高质量图像-文本推理数据稀缺的挑战。虽然纯文本推理资源丰富且易于扩展，但如何有效地利用这些资源来提升VLM的推理能力仍然是一个开放性问题。现有方法难以充分利用文本推理资源，且在数据稀缺的情况下泛化能力有限。

**核心思路**：VOLD的核心思路是通过在线策略蒸馏，将纯文本教师模型（LLM）的推理能力迁移到VLM学生模型。具体来说，利用教师模型生成的推理轨迹来指导学生模型的学习过程，从而使学生模型能够模仿教师模型的推理策略，提升其在视觉-语言推理任务中的性能。这种方法充分利用了丰富的文本推理资源，并克服了数据稀缺带来的挑战。

**技术框架**：VOLD框架主要包含以下几个关键模块：1) 教师模型（纯文本LLM）：负责生成推理轨迹，提供推理指导。2) 学生模型（VLM）：负责学习教师模型的推理策略，并在视觉-语言推理任务中进行推理。3) 基于群体相对策略优化(GRPO)的强化学习：用于优化学生模型的策略，使其更好地模仿教师模型的推理轨迹。4) 在线策略蒸馏：利用教师模型的推理轨迹来指导学生模型的学习过程，实现知识迁移。5) 冷启动对齐：通过监督微调(SFT)对学生模型进行预训练，使其与教师模型具有相似的分布，从而提高在线策略蒸馏的有效性。

**关键创新**：VOLD的关键创新在于结合了强化学习和在线策略蒸馏，实现从纯文本教师模型到VLM学生模型的推理能力迁移。与传统的离线蒸馏方法不同，VOLD采用在线策略蒸馏，可以动态地利用教师模型的推理轨迹来指导学生模型的学习过程，从而更有效地迁移知识。此外，VOLD还引入了冷启动对齐，通过监督微调(SFT)对学生模型进行预训练，使其与教师模型具有相似的分布，从而提高在线策略蒸馏的有效性。

**关键设计**：VOLD的关键设计包括：1) 使用Group Relative Policy Optimization (GRPO) 作为强化学习算法，优化学生模型的策略。2) 使用KL散度作为蒸馏损失，衡量学生模型和教师模型之间的策略差异。3) 通过监督微调(SFT)进行冷启动对齐，使用文本数据对学生模型进行预训练，使其与教师模型具有相似的分布。4) 在线策略蒸馏过程中，动态调整蒸馏损失的权重，以平衡探索和利用。

## 📊 实验亮点

VOLD在MMMU-Pro、MathVision、MathVista和LogicVista等多个基准测试中取得了显著的性能提升。例如，在MMMU-Pro上，VOLD的性能超过基线模型，并在现有技术水平上有所提高。消融实验表明，冷启动对齐对于在线策略蒸馏至关重要，验证了VOLD框架的有效性。

## 🎯 应用场景

VOLD框架具有广泛的应用前景，可用于提升VLM在各种复杂推理任务中的性能，例如视觉问答、图像描述、视觉推理等。该研究成果有助于开发更智能、更强大的多模态人工智能系统，可应用于智能助手、自动驾驶、医疗诊断等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Training vision-language models (VLMs) for complex reasoning remains a challenging task, i.a. due to the scarcity of high-quality image-text reasoning data. Conversely, text-based reasoning resources are abundant and scalable, but it is still an open question how to leveraging them for VLM reasoning. To address this problem, we propose VOLD, a framework to transfer reasoning capabilities from text-only teacher models to VLM student models. To this end, VOLD combines reinforcement learning via Group Relative Policy Optimization (GRPO) with on-policy distillation, which allows the student reasoning traces to be guided by the teacher model, resulting in a significant gain over using GRPO alone. We further show that a cold-start alignment is essential for an effective transfer during the online training phase in this scenario and that without sufficient distributional alignment between teacher and student, on-policy distillation fails to provide meaningful guidance. We evaluate VOLD across diverse benchmarks including MMMU-Pro, MathVision, MathVista, and LogicVista, showing that VOLD outperforms the baseline model significantly and improves over the state of the art by a margin. Our ablation shows the importance of a cold-start alignment via SFT for on-policy distillation with a text-only teacher.

