---
layout: default
title: "SCOPE: Semantic Conditioning for Sim2Real Category-Level Object Pose Estimation in Robotics"
---

# SCOPE: Semantic Conditioning for Sim2Real Category-Level Object Pose Estimation in Robotics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24572" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24572v1</a>
  <a href="https://arxiv.org/pdf/2509.24572.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24572v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24572v1', 'SCOPE: Semantic Conditioning for Sim2Real Category-Level Object Pose Estimation in Robotics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peter Hönig, Stefan Thalhammer, Jean-Baptiste Weibel, Matthias Hirschmanner, Markus Vincze

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-29

**🔗 代码/项目**: [GITHUB](https://github.com/hoenigpeter/scope)

---

## 💡 一句话要点

**SCOPE：基于语义条件扩散模型的机器人Sim2Real类别级物体姿态估计**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `物体姿态估计` `类别级估计` `Sim2Real` `扩散模型` `DINOv2` `语义先验` `机器人操作`

## 📋 核心要点

1. 现有物体操作方法在开放环境中难以处理未知物体，需要语义理解以泛化到已知类别之外。
2. SCOPE利用DINOv2特征作为连续语义先验，结合扩散模型进行类别级物体姿态估计，无需离散类别标签。
3. SCOPE在合成数据训练中超越现有技术，并在实例级数据集上展示了对未知物体的抓取能力。

## 📝 摘要（中文）

本文提出SCOPE，一种基于扩散模型的类别级物体姿态估计方法，通过利用DINOv2特征作为连续语义先验，消除了对离散类别标签的需求。结合逼真的训练数据和点法线的噪声模型，SCOPE缩小了类别级物体姿态估计中的Sim2Real差距。通过交叉注意力注入连续语义先验，SCOPE能够学习跨越已知类别分布之外的物体实例的规范化物体坐标系。在合成训练的类别级物体姿态估计中，SCOPE优于当前最先进的方法，在5°5cm指标上实现了31.9%的相对改进。在两个实例级数据集上的实验表明，该方法能够泛化到已知物体类别之外，从而能够以高达100%的成功率抓取未知类别的未见物体。

## 🔬 方法详解

**问题定义**：现有类别级物体姿态估计方法通常依赖于离散的类别标签，这限制了它们在开放环境中处理未知物体的能力。Sim2Real差距也是一个挑战，因为在仿真环境中训练的模型难以直接应用于真实世界。

**核心思路**：SCOPE的核心思路是利用DINOv2特征作为连续的语义先验，取代离散的类别标签。通过将语义信息融入到扩散模型中，SCOPE能够学习到跨越不同类别和实例的物体姿态表示，从而实现更好的泛化能力。此外，使用逼真的训练数据和点法线的噪声模型来缩小Sim2Real差距。

**技术框架**：SCOPE的整体框架包含以下几个主要模块：1) DINOv2特征提取器，用于提取输入点云的语义特征；2) 扩散模型，用于生成物体姿态的候选解；3) 交叉注意力机制，用于将DINOv2特征注入到扩散模型的生成过程中；4) 损失函数，用于优化模型的参数，包括姿态损失和语义一致性损失。

**关键创新**：SCOPE最重要的技术创新在于使用连续的语义先验（DINOv2特征）来指导物体姿态估计，而不是依赖于离散的类别标签。这使得模型能够更好地泛化到未知物体和类别。此外，通过交叉注意力机制将语义信息融入到扩散模型中，可以有效地利用语义信息来提高姿态估计的准确性。

**关键设计**：SCOPE的关键设计包括：1) 使用逼真的合成数据进行训练，以减少Sim2Real差距；2) 引入点法线的噪声模型，以提高模型对噪声的鲁棒性；3) 使用交叉注意力机制将DINOv2特征注入到扩散模型的生成过程中；4) 设计合适的损失函数，包括姿态损失和语义一致性损失，以优化模型的参数。

## 📊 实验亮点

SCOPE在合成训练的类别级物体姿态估计中取得了显著的性能提升，在5°5cm指标上实现了31.9%的相对改进。此外，在两个实例级数据集上的实验表明，SCOPE能够成功抓取未知类别的未见物体，成功率高达100%，展示了其强大的泛化能力。

## 🎯 应用场景

SCOPE在机器人操作领域具有广泛的应用前景，例如智能仓储、自动化装配、家庭服务机器人等。它可以帮助机器人在开放环境中识别和抓取各种物体，即使这些物体是未知的或属于新的类别。该研究的成果可以提高机器人的自主性和适应性，使其能够更好地完成各种任务。

## 📄 摘要（原文）

> Object manipulation requires accurate object pose estimation. In open environments, robots encounter unknown objects, which requires semantic understanding in order to generalize both to known categories and beyond. To resolve this challenge, we present SCOPE, a diffusion-based category-level object pose estimation model that eliminates the need for discrete category labels by leveraging DINOv2 features as continuous semantic priors. By combining these DINOv2 features with photorealistic training data and a noise model for point normals, we reduce the Sim2Real gap in category-level object pose estimation. Furthermore, injecting the continuous semantic priors via cross-attention enables SCOPE to learn canonicalized object coordinate systems across object instances beyond the distribution of known categories. SCOPE outperforms the current state of the art in synthetically trained category-level object pose estimation, achieving a relative improvement of 31.9\% on the 5$^\circ$5cm metric. Additional experiments on two instance-level datasets demonstrate generalization beyond known object categories, enabling grasping of unseen objects from unknown categories with a success rate of up to 100\%. Code available: https://github.com/hoenigpeter/scope.

