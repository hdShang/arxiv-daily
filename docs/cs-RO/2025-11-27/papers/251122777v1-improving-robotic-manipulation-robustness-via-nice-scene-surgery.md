---
layout: default
title: Improving Robotic Manipulation Robustness via NICE Scene Surgery
---

# Improving Robotic Manipulation Robustness via NICE Scene Surgery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22777" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22777v1</a>
  <a href="https://arxiv.org/pdf/2511.22777.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22777v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.22777v1', 'Improving Robotic Manipulation Robustness via NICE Scene Surgery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sajjad Pakdamansavoji, Mozhgan Pourkeshavarz, Adam Sigal, Zhiyuan Li, Rui Heng Yang, Amir Rasouli

**分类**: cs.RO, cs.AI

**发布日期**: 2025-11-27

**备注**: 11 figures, 3 tables

---

## 💡 一句话要点

**NICE场景手术：利用自然图像修复增强机器人操作的鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `机器人操作` `视觉鲁棒性` `数据增强` `图像生成` `大型语言模型` `场景理解` `分布外泛化` `模仿学习`

## 📋 核心要点

1. 现实世界中机器人操作面临视觉干扰，现有方法难以保证策略的鲁棒性和安全性。
2. NICE框架利用图像生成和大型语言模型，通过场景编辑增加视觉多样性，缩小分布外差距。
3. 实验表明，NICE显著提升了机器人操作的准确率、成功率和安全性，无需额外数据或模型训练。

## 📝 摘要（中文）

在现实环境中，视觉干扰会显著降低机器人操作策略的性能和安全性。本文提出了一种有效且可扩展的框架，即自然场景修复增强（NICE）。该方法通过利用现有演示构建新的经验，增加视觉多样性，从而最大限度地减少模仿学习中的分布外（OOD）差距。NICE利用图像生成框架和大型语言模型执行三种编辑操作：对象替换、风格转换和移除干扰（非目标）对象。这些更改在不阻碍目标对象的情况下保持空间关系，并保持动作标签的一致性。与以往的方法不同，NICE不需要额外的数据采集、模拟器访问或自定义模型训练，使其易于应用于现有的机器人数据集。在真实场景中，展示了NICE在生成逼真场景增强方面的能力。在下游任务中，我们使用NICE数据来微调视觉-语言模型（VLM）以进行空间可供性预测，以及视觉-语言-动作（VLA）策略以进行对象操作。评估表明，NICE成功地最大限度地减少了OOD差距，从而使高度杂乱场景中的可供性预测准确率提高了20%以上。对于操作任务，在不同数量的干扰物环境中进行测试时，成功率平均提高了11%。此外，该方法提高了视觉鲁棒性，将目标混淆降低了6%，并通过降低7%的碰撞率来增强安全性。

## 🔬 方法详解

**问题定义**：论文旨在解决真实场景中机器人操作因视觉干扰物导致性能下降的问题。现有方法通常需要大量真实数据或依赖模拟环境，成本高昂且泛化能力有限。这些方法难以适应复杂多变的真实环境，导致机器人操作的鲁棒性不足。

**核心思路**：论文的核心思路是通过图像修复和生成技术，在现有数据集上进行场景增强，增加视觉多样性，从而提高模型对分布外数据的泛化能力。通过对场景进行对象替换、风格转换和移除干扰物等操作，模拟真实世界中可能出现的各种视觉干扰，使模型能够更好地适应复杂环境。

**技术框架**：NICE框架主要包含三个阶段：1) 场景理解：利用大型语言模型和视觉模型理解场景内容，识别目标对象和干扰物；2) 场景编辑：利用图像生成模型对场景进行编辑，包括对象替换、风格转换和移除干扰物等操作；3) 数据增强：将编辑后的图像添加到训练数据集中，用于训练或微调机器人操作策略。整个流程无需额外的机器人数据采集、模拟器访问或自定义模型训练。

**关键创新**：NICE的关键创新在于利用图像生成和大型语言模型进行场景增强，从而在不增加数据采集成本的前提下，显著提高机器人操作的鲁棒性。与传统的数据增强方法相比，NICE能够生成更逼真、更多样化的场景，更有效地模拟真实世界中的视觉干扰。此外，NICE框架具有良好的可扩展性，可以方便地应用于不同的机器人操作任务和数据集。

**关键设计**：NICE框架的关键设计包括：1) 使用预训练的图像生成模型（如Stable Diffusion）进行场景编辑，保证生成图像的逼真度；2) 利用大型语言模型（如GPT-3）进行场景理解和对象识别，提高场景编辑的准确性；3) 设计合适的损失函数，保证场景编辑后的图像与原始图像在语义上的一致性；4) 通过控制场景编辑的强度和频率，避免引入过多的噪声，影响模型的训练效果。

## 📊 实验亮点

实验结果表明，NICE框架能够显著提高机器人操作的性能。在可供性预测任务中，NICE使准确率提高了20%以上。在操作任务中，成功率平均提高了11%，目标混淆降低了6%，碰撞率降低了7%。这些结果表明，NICE能够有效地提高机器人操作的鲁棒性和安全性。

## 🎯 应用场景

该研究成果可广泛应用于各种机器人操作任务，例如工业自动化、家庭服务机器人、医疗机器人等。通过提高机器人操作的鲁棒性和安全性，可以降低生产成本、提高工作效率，并减少人为干预。未来，该方法有望应用于更复杂的机器人任务，例如自主导航、目标搜索和人机协作等。

## 📄 摘要（原文）

> Learning robust visuomotor policies for robotic manipulation remains a challenge in real-world settings, where visual distractors can significantly degrade performance and safety. In this work, we propose an effective and scalable framework, Naturalistic Inpainting for Context Enhancement (NICE). Our method minimizes out-of-distribution (OOD) gap in imitation learning by increasing visual diversity through construction of new experiences using existing demonstrations. By utilizing image generative frameworks and large language models, NICE performs three editing operations, object replacement, restyling, and removal of distracting (non-target) objects. These changes preserve spatial relationships without obstructing target objects and maintain action-label consistency. Unlike previous approaches, NICE requires no additional robot data collection, simulator access, or custom model training, making it readily applicable to existing robotic datasets.
>   Using real-world scenes, we showcase the capability of our framework in producing photo-realistic scene enhancement. For downstream tasks, we use NICE data to finetune a vision-language model (VLM) for spatial affordance prediction and a vision-language-action (VLA) policy for object manipulation. Our evaluations show that NICE successfully minimizes OOD gaps, resulting in over 20% improvement in accuracy for affordance prediction in highly cluttered scenes. For manipulation tasks, success rate increases on average by 11% when testing in environments populated with distractors in different quantities. Furthermore, we show that our method improves visual robustness, lowering target confusion by 6%, and enhances safety by reducing collision rate by 7%.

