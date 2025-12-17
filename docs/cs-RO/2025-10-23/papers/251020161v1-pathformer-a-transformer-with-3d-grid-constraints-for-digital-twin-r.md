---
layout: default
title: PathFormer: A Transformer with 3D Grid Constraints for Digital Twin Robot-Arm Trajectory Generation
---

# PathFormer: A Transformer with 3D Grid Constraints for Digital Twin Robot-Arm Trajectory Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20161" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20161v1</a>
  <a href="https://arxiv.org/pdf/2510.20161.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20161v1" onclick="toggleFavorite(this, '2510.20161v1', 'PathFormer: A Transformer with 3D Grid Constraints for Digital Twin Robot-Arm Trajectory Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahmed Alanazi, Duy Ho, Yugyung Lee

**分类**: cs.RO

**发布日期**: 2025-10-23

**备注**: 8 pages, 7 figures, 7 tables

---

## 💡 一句话要点

**PathFormer：结合3D网格约束的Transformer用于数字孪生机器人手臂轨迹生成**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人手臂` `轨迹规划` `Transformer` `3D网格` `数字孪生`

## 📋 核心要点

1. 现有序列模型在机器人手臂轨迹规划中忽略运动结构，导致轨迹无效或效率低下。
2. PathFormer通过3D网格表示编码机器人运动，并使用约束掩码解码，保证轨迹的合法性。
3. 实验表明，PathFormer在轨迹准确性、触达率和拾取成功率方面均表现出色，并具备良好的泛化能力。

## 📝 摘要（中文）

机器人手臂需要精确且任务感知的轨迹规划，但忽略运动结构的序列模型通常产生无效或低效的执行。本文提出了一种基于路径的Transformer，它使用3D网格（where/what/when）表示编码机器人运动，并采用约束掩码解码，在推理任务图和动作顺序的同时，强制执行格子相邻移动和工作空间边界。在53755条轨迹（80%训练/20%验证）上训练的模型与真实情况高度吻合——步进准确率为89.44%，精确率为93.32%，召回率为89.44%，F1值为90.40%——并且通过构造保证99.99%的路径合法性。在配备深度相机数字孪生的xArm Lite 6上编译为运动原语后，在受控测试中达到高达97.5%的触达率和92.5%的拾取成功率，并在杂乱场景中跨60个语言指定的任务中达到86.7%的端到端成功率，通过局部重新定位吸收滑动和遮挡，而无需全局重新规划。这些结果表明，路径结构化表示使Transformer能够生成准确、可靠和可解释的机器人轨迹，桥接了基于图的规划和基于序列的学习，并为通用操作和sim-to-real迁移提供了实践基础。

## 🔬 方法详解

**问题定义**：机器人手臂轨迹规划需要精确且任务感知的运动，现有序列模型缺乏对运动结构的建模能力，容易生成不符合物理约束或效率低下的轨迹。这些方法难以保证轨迹的合法性，并且在复杂环境中泛化能力较弱。

**核心思路**：本文的核心思路是将机器人运动表示为3D网格（where/what/when），利用Transformer模型学习轨迹的序列依赖关系，并通过约束掩码解码保证轨迹的合法性。这种方法结合了图规划和序列学习的优点，能够生成更准确、可靠和可解释的机器人轨迹。

**技术框架**：PathFormer的整体框架包括以下几个主要模块：1) 3D网格编码器：将机器人运动状态编码为3D网格表示；2) Transformer编码器：学习轨迹的序列依赖关系；3) 约束掩码解码器：生成符合物理约束的轨迹；4) 运动原语编译器：将生成的轨迹编译为机器人可执行的运动原语。

**关键创新**：PathFormer的关键创新在于：1) 提出了一种基于3D网格的机器人运动表示方法，能够有效地捕捉运动结构信息；2) 引入了约束掩码解码机制，保证生成的轨迹符合物理约束；3) 将Transformer模型应用于机器人轨迹规划，充分利用了Transformer强大的序列建模能力。

**关键设计**：PathFormer的关键设计包括：1) 3D网格的分辨率和范围；2) Transformer的层数和隐藏层大小；3) 约束掩码的类型和强度；4) 损失函数的设计，包括轨迹准确性损失和约束违反损失。

## 📊 实验亮点

PathFormer在53755条轨迹上训练后，步进准确率达到89.44%，精确率达到93.32%，召回率达到89.44%，F1值达到90.40%，并且通过构造保证99.99%的路径合法性。在xArm Lite 6上进行实验，在受控测试中达到高达97.5%的触达率和92.5%的拾取成功率，并在杂乱场景中跨60个语言指定的任务中达到86.7%的端到端成功率。

## 🎯 应用场景

PathFormer可应用于各种机器人手臂轨迹规划场景，例如工业自动化、医疗机器人、服务机器人等。该研究成果有助于提高机器人手臂的运动精度、可靠性和安全性，并为通用操作和sim-to-real迁移提供技术支持，具有重要的实际应用价值和广阔的未来发展前景。

## 📄 摘要（原文）

> Robotic arms require precise, task-aware trajectory planning, yet sequence models that ignore motion structure often yield invalid or inefficient executions. We present a Path-based Transformer that encodes robot motion with a 3-grid (where/what/when) representation and constraint-masked decoding, enforcing lattice-adjacent moves and workspace bounds while reasoning over task graphs and action order. Trained on 53,755 trajectories (80% train / 20% validation), the model aligns closely with ground truth -- 89.44% stepwise accuracy, 93.32% precision, 89.44% recall, and 90.40% F1 -- with 99.99% of paths legal by construction. Compiled to motor primitives on an xArm Lite 6 with a depth-camera digital twin, it attains up to 97.5% reach and 92.5% pick success in controlled tests, and 86.7% end-to-end success across 60 language-specified tasks in cluttered scenes, absorbing slips and occlusions via local re-grounding without global re-planning. These results show that path-structured representations enable Transformers to generate accurate, reliable, and interpretable robot trajectories, bridging graph-based planning and sequence-based learning and providing a practical foundation for general-purpose manipulation and sim-to-real transfer.

