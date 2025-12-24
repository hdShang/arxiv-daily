---
layout: default
title: X2C: A Dataset Featuring Nuanced Facial Expressions for Realistic Humanoid Imitation
---

# X2C: A Dataset Featuring Nuanced Facial Expressions for Realistic Humanoid Imitation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11146" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11146v2</a>
  <a href="https://arxiv.org/pdf/2505.11146.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11146v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11146v2', 'X2C: A Dataset Featuring Nuanced Facial Expressions for Realistic Humanoid Imitation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peizhen Li, Longbing Cao, Xiao-Ming Wu, Runze Yang, Xiaohan Yu

**分类**: cs.RO, cs.AI, cs.HC

**发布日期**: 2025-05-16 (更新: 2025-09-20)

**🔗 代码/项目**: [PROJECT_PAGE](https://lipzh5.github.io/X2CNet/)

---

## 💡 一句话要点

**提出X2C数据集以解决人形机器人面部表情模仿问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `人形机器人` `面部表情` `情感交互` `数据集` `深度学习` `表情模仿` `X2CNet`

## 📋 核心要点

1. 现有方法缺乏多样化和高质量的面部表情数据集，限制了人形机器人在情感交互中的表现。
2. 提出X2C数据集，包含100,000对图像和控制值，及X2CNet框架，实现人到人形的面部表情模仿。
3. 通过在真实人形机器人上的演示，验证了X2CNet的有效性，为人形表情模仿任务提供了基线。

## 📝 摘要（中文）

人形机器人在情感人机交互中模仿真实面部表情的能力至关重要。然而，缺乏包含多样化人形面部表情及适当注释的数据集，阻碍了真实人形面部表情模仿的进展。为了解决这些挑战，我们引入了X2C（Anything to Control）数据集，包含细腻的面部表情以实现真实的人形模仿。X2C提供了高质量、高多样性的大规模数据集，包含100,000对（图像，控制值），每张图像展示了人形机器人表现出的多样化面部表情，并注释了30个控制值，代表真实的表情配置。同时，我们提出了X2CNet，一个新的人到人形面部表情模仿框架，能够学习细腻的人形表情与其控制值之间的对应关系，并在真实的人形机器人上进行了演示，展示了其在真实人形面部表情模仿中的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决人形机器人在情感交互中缺乏多样化面部表情数据集的问题。现有方法未能提供足够的注释数据，限制了机器人表情模仿的真实感和多样性。

**核心思路**：论文提出了X2C数据集和X2CNet框架，旨在通过高质量的图像和控制值对，学习人类与人形机器人之间的面部表情对应关系，从而实现更自然的表情模仿。

**技术框架**：整体架构包括数据集构建和模型训练两个主要阶段。数据集阶段收集并注释了多样化的面部表情图像，模型训练阶段则利用这些数据进行深度学习，学习表情与控制值之间的映射关系。

**关键创新**：最重要的技术创新在于X2C数据集的构建和X2CNet框架的提出，前者提供了丰富的面部表情样本，后者则实现了人类与人形机器人之间的表情模仿，填补了现有研究的空白。

**关键设计**：在数据集构建中，采用了30个控制值来准确表示表情配置；在模型设计中，使用了深度学习技术来优化表情模仿的效果，具体的损失函数和网络结构设计尚未详细披露。

## 📊 实验亮点

实验结果表明，X2CNet在多种人类表演者的面部表情模仿任务中表现出色，能够有效地实现高质量的表情再现。具体性能数据尚未披露，但通过真实人形机器人的演示，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括人形机器人、虚拟助手和情感计算等。通过提高人形机器人的面部表情模仿能力，可以增强人机交互的自然性和情感表达，从而在教育、医疗和娱乐等多个领域产生深远影响。

## 📄 摘要（原文）

> The ability to imitate realistic facial expressions is essential for humanoid robots engaged in affective human-robot communication. However, the lack of datasets containing diverse humanoid facial expressions with proper annotations hinders progress in realistic humanoid facial expression imitation. To address these challenges, we introduce X2C (Anything to Control), a dataset featuring nuanced facial expressions for realistic humanoid imitation. With X2C, we contribute: 1) a high-quality, high-diversity, large-scale dataset comprising 100,000 (image, control value) pairs. Each image depicts a humanoid robot displaying a diverse range of facial expressions, annotated with 30 control values representing the ground-truth expression configuration; 2) X2CNet, a novel human-to-humanoid facial expression imitation framework that learns the correspondence between nuanced humanoid expressions and their underlying control values from X2C. It enables facial expression imitation in the wild for different human performers, providing a baseline for the imitation task, showcasing the potential value of our dataset; 3) real-world demonstrations on a physical humanoid robot, highlighting its capability to advance realistic humanoid facial expression imitation. Code and Data: https://lipzh5.github.io/X2CNet/

