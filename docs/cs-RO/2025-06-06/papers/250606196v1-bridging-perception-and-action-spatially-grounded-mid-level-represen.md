---
layout: default
title: "Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization"
---

# Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06196" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06196v1</a>
  <a href="https://arxiv.org/pdf/2506.06196.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06196v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06196v1', 'Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonathan Yang, Chuyuan Kelly Fu, Dhruv Shah, Dorsa Sadigh, Fei Xia, Tingnan Zhang

**分类**: cs.RO

**发布日期**: 2025-06-06

**备注**: 16 pages, 13 figures

---

## 💡 一句话要点

**提出空间基础的中层表示以提升机器人任务的泛化能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人学习` `策略优化` `中层表示` `灵巧操作` `专家模型` `模仿学习` `深度学习`

## 📋 核心要点

1. 现有方法在灵巧任务的策略学习和泛化能力上存在不足，缺乏有效的中层表示来提供可操作的信息。
2. 本研究提出了一种新颖的专家混合策略架构，结合多个专门的模型，通过中层表示来提升策略学习的效果。
3. 实验结果表明，该方法在评估任务中成功率比基线提高了11%至24%，并通过加权模仿学习进一步提升了10%的性能。

## 📝 摘要（中文）

本研究探讨了空间基础的辅助表示如何提供广泛的高层次基础以及直接的可操作信息，以改善策略学习性能和对灵巧任务的泛化能力。我们在对象中心性、姿态意识和深度意识三个关键维度上研究这些中层表示。通过监督学习训练专门的编码器，并将其作为输入提供给扩散策略，以解决现实世界中的双手灵巧操作任务。我们提出了一种新颖的专家混合策略架构，结合多个在不同中层表示上训练的专家模型，以提高策略的泛化能力。该方法在评估任务中实现了比语言基础基线高11%和比标准扩散策略基线高24%的平均成功率。此外，利用中层表示作为加权模仿学习算法中的监督信号，进一步提高了策略对这些表示的跟随精度，性能提升达10%。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人在灵巧任务中策略学习和泛化能力不足的问题。现有方法通常依赖于高层次的感知信息，缺乏对具体操作的细致指导，导致性能受限。

**核心思路**：论文提出通过空间基础的中层表示来改善策略学习，强调不仅需要广泛的感知任务基础，还需更细致的可操作表示，以增强策略的有效性和泛化能力。

**技术框架**：整体架构包括三个主要模块：首先，使用监督学习训练专门的编码器以提取中层表示；其次，将这些中层表示作为输入传递给扩散策略；最后，采用混合专家策略架构，结合多个在不同中层表示上训练的专家模型。

**关键创新**：最重要的技术创新在于提出了混合专家策略架构，通过结合多个专门模型来提升策略的泛化能力，这一方法与现有的单一模型策略有本质区别。

**关键设计**：在设计中，采用了加权模仿学习算法，将中层表示作为监督信号，优化了策略的跟随精度。此外，模型的训练过程中，针对不同的中层表示设置了不同的损失函数，以确保每个专家模型的有效性。

## 📊 实验亮点

实验结果显示，提出的方法在评估任务中实现了比语言基础基线高11%和比标准扩散策略基线高24%的成功率。此外，利用中层表示作为监督信号的加权模仿学习算法，使得策略的跟随精度提升了10%。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造、服务机器人等。通过提升机器人在复杂任务中的泛化能力，能够更好地适应动态环境，执行多样化的操作任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In this work, we investigate how spatially grounded auxiliary representations can provide both broad, high-level grounding as well as direct, actionable information to improve policy learning performance and generalization for dexterous tasks. We study these mid-level representations across three critical dimensions: object-centricity, pose-awareness, and depth-awareness. We use these interpretable mid-level representations to train specialist encoders via supervised learning, then feed them as inputs to a diffusion policy to solve dexterous bimanual manipulation tasks in the real world. We propose a novel mixture-of-experts policy architecture that combines multiple specialized expert models, each trained on a distinct mid-level representation, to improve policy generalization. This method achieves an average success rate that is 11% higher than a language-grounded baseline and 24 percent higher than a standard diffusion policy baseline on our evaluation tasks. Furthermore, we find that leveraging mid-level representations as supervision signals for policy actions within a weighted imitation learning algorithm improves the precision with which the policy follows these representations, yielding an additional performance increase of 10%. Our findings highlight the importance of grounding robot policies not only with broad perceptual tasks but also with more granular, actionable representations. For further information and videos, please visit https://mid-level-moe.github.io.

