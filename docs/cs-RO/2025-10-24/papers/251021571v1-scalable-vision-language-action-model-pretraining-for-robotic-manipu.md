---
layout: default
title: Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos
---

# Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21571" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21571v1</a>
  <a href="https://arxiv.org/pdf/2510.21571.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21571v1" onclick="toggleFavorite(this, '2510.21571v1', 'Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qixiu Li, Yu Deng, Yaobo Liang, Lin Luo, Lei Zhou, Chengtang Yao, Lingqi Zeng, Zhiyuan Feng, Huizhi Liang, Sicheng Xu, Yizhong Zhang, Xi Chen, Hao Chen, Lily Sun, Dong Chen, Jiaolong Yang, Baining Guo

**分类**: cs.RO, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-10-24

**备注**: Project page: https://microsoft.github.io/VITRA/

---

## 💡 一句话要点

**提出基于大规模真实人类活动视频的机器人操作VLA模型预训练方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `视觉-语言-动作模型` `预训练` `人类活动视频` `具身智能`

## 📋 核心要点

1. 现有机器人操作学习依赖于有限的、标注成本高的机器人数据，泛化性不足。
2. 利用大规模无标注的人类活动视频，通过自动化分析生成VLA数据，模拟机器人操作场景。
3. 预训练的VLA模型在零样本任务中表现出色，微调后显著提升了真实机器人任务的成功率。

## 📝 摘要（中文）

本文提出了一种新颖的方法，利用大量未经标注的真实人类手部活动视频记录，对机器人操作的视觉-语言-动作（VLA）模型进行预训练。通过将人类手部视为灵巧的机器人末端执行器，我们展示了“野外”的以自我为中心的人类视频可以被转换成与现有机器人VLA训练数据完全对齐的数据格式，包括任务粒度和标签。这通过开发一种全自动的整体人类活动分析方法来实现，该方法能够生成原子级别的手部活动片段及其语言描述，并伴随逐帧的3D手部运动和相机运动。我们处理了大量的以自我为中心的视频，并创建了一个包含100万个片段和2600万帧的手部VLA训练数据集。该训练数据涵盖了真实生活中的各种物体和概念、灵巧的操作任务以及环境变化，大大超过了现有机器人数据的覆盖范围。我们设计了一个灵巧的手部VLA模型架构，并在此数据集上对模型进行预训练。该模型在完全未见过的真实世界观察中表现出强大的零样本能力。此外，在少量真实机器人动作数据上对其进行微调，可以显著提高任务成功率和对真实机器人实验中新物体的泛化能力。我们还展示了模型任务性能相对于预训练数据规模的吸引人的缩放行为。我们相信这项工作为可扩展的VLA预训练奠定了坚实的基础，推动机器人朝着真正可泛化的具身智能发展。

## 🔬 方法详解

**问题定义**：现有机器人操作学习方法依赖于有限的、成本高昂的机器人数据，导致模型泛化能力不足，难以适应真实世界中复杂多变的环境和任务。如何利用更广泛的数据源，提升机器人操作模型的泛化性和适应性，是本文要解决的核心问题。

**核心思路**：本文的核心思路是将人类手部活动视为灵巧的机器人末端执行器，利用大量未经标注的真实人类活动视频，通过自动化分析生成与机器人VLA训练数据格式对齐的数据。这种方法能够有效地扩展训练数据的规模和多样性，从而提升模型的泛化能力。

**技术框架**：整体框架包括以下几个主要模块：1) 大规模人类活动视频收集；2) 全自动人类活动分析，包括手部活动分割、语言描述生成、3D手部运动和相机运动估计；3) 基于生成的数据集进行VLA模型预训练；4) 在真实机器人数据上进行微调；5) 评估模型在零样本和微调后的性能。

**关键创新**：最重要的技术创新点在于提出了一种全自动的人类活动分析方法，能够将任意人类手部视频转化为机器人VLA训练数据。与现有方法相比，该方法无需人工标注，能够处理大规模的真实世界视频，从而显著扩展了训练数据的规模和多样性。

**关键设计**：关键设计包括：1) 设计了适用于灵巧手部操作的VLA模型架构；2) 开发了能够准确分割手部活动片段并生成自然语言描述的算法；3) 采用了有效的3D手部运动和相机运动估计方法；4) 设计了合适的损失函数和训练策略，以充分利用大规模预训练数据。

## 📊 实验亮点

实验结果表明，在预训练数据集上训练的VLA模型在零样本任务中表现出强大的能力。在少量真实机器人数据上进行微调后，任务成功率显著提高，并且对新物体的泛化能力也得到了提升。此外，实验还验证了模型性能随预训练数据规模的增加而提升的缩放行为。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，例如家庭服务机器人、工业自动化机器人和医疗辅助机器人。通过利用大规模人类活动视频进行预训练，可以显著降低机器人学习的成本，提高机器人的泛化能力和适应性，使其能够更好地完成各种复杂的操作任务。未来，该方法有望推动机器人技术在更广泛的领域得到应用。

## 📄 摘要（原文）

> This paper presents a novel approach for pretraining robotic manipulation Vision-Language-Action (VLA) models using a large corpus of unscripted real-life video recordings of human hand activities. Treating human hand as dexterous robot end-effector, we show that "in-the-wild" egocentric human videos without any annotations can be transformed into data formats fully aligned with existing robotic V-L-A training data in terms of task granularity and labels. This is achieved by the development of a fully-automated holistic human activity analysis approach for arbitrary human hand videos. This approach can generate atomic-level hand activity segments and their language descriptions, each accompanied with framewise 3D hand motion and camera motion. We process a large volume of egocentric videos and create a hand-VLA training dataset containing 1M episodes and 26M frames. This training data covers a wide range of objects and concepts, dexterous manipulation tasks, and environment variations in real life, vastly exceeding the coverage of existing robot data. We design a dexterous hand VLA model architecture and pretrain the model on this dataset. The model exhibits strong zero-shot capabilities on completely unseen real-world observations. Additionally, fine-tuning it on a small amount of real robot action data significantly improves task success rates and generalization to novel objects in real robotic experiments. We also demonstrate the appealing scaling behavior of the model's task performance with respect to pretraining data scale. We believe this work lays a solid foundation for scalable VLA pretraining, advancing robots toward truly generalizable embodied intelligence.

