---
layout: default
title: "Decoupled Action Head: Confining Task Knowledge to Conditioning Layers"
---

# Decoupled Action Head: Confining Task Knowledge to Conditioning Layers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.12101" class="toolbar-btn" target="_blank">📄 arXiv: 2511.12101v1</a>
  <a href="https://arxiv.org/pdf/2511.12101.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12101v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.12101v1', 'Decoupled Action Head: Confining Task Knowledge to Conditioning Layers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Zhou, Sihao Lin, Shuai Fu, Qi WU

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-11-15

---

## 💡 一句话要点

**提出解耦行为克隆训练方法，提升机器人操作任务的训练效率与泛化性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `行为克隆` `机器人操作` `解耦训练` `扩散策略` `动作生成` `特征调制` `模型加速`

## 📋 核心要点

1. 行为克隆方法在机器人操作中受限于配对训练数据的稀缺，且内部机制不够明确，导致泛化性不足。
2. 提出解耦训练方案，利用运动学生成的轨迹预训练通用动作头，然后冻结并适应新任务，实现知识迁移。
3. 实验表明该方法在同分布和异分布场景中可行，并显著提升训练效率，同时验证了动作生成骨干网络的重要性较低。

## 📝 摘要（中文）

行为克隆(BC)是一种数据驱动的监督学习方法，随着语言和视觉领域缩放定律的成功，它受到了越来越多的关注。在机器人操作的实现中，扩散策略(DP)及其两个变体DP-CNN (DP-C)和DP-Transformer (DP-T)是最有效和广泛采用的模型之一，展示了预测连续动作序列的优势。然而，DP和其他BC方法仍然受到配对训练数据稀缺的限制，并且DP有效性的内部机制仍然不够明确，导致泛化能力有限，并且在模型开发中缺乏原则性设计。在这项工作中，我们提出了一种解耦训练方案，该方案利用几乎无成本的运动学生成的轨迹作为无观察数据来预训练通用动作头(动作生成器)。然后，冻结预训练的动作头，并通过特征调制使其适应新的任务。我们的实验证明了这种方法在同分布和异分布场景中的可行性。作为额外的好处，解耦提高了训练效率；例如，DP-C实现了高达41%的加速。此外，在解耦下，任务特定知识被限制在调节组件中，再加上DP-C在正常和解耦训练中几乎相同的性能，表明动作生成骨干在机器人操作中起到的作用有限。受此观察的启发，我们引入了DP-MLP，它用仅4M参数的简单MLP块替换了DP-C的244M参数U-Net骨干，在正常训练下实现了83.9%的更快训练速度，在解耦下实现了89.1%的更快训练速度。

## 🔬 方法详解

**问题定义**：现有的行为克隆方法，如Diffusion Policy (DP)，在机器人操作任务中面临训练数据稀缺的问题，导致模型泛化能力受限。同时，DP内部有效性的机制尚不明确，缺乏指导模型设计的理论基础。

**核心思路**：论文的核心思路是将动作生成与任务特定知识解耦。通过预训练一个通用的动作生成器，使其学习生成合理的动作序列，然后通过特征调制的方式将该动作生成器适配到不同的任务中。这样可以利用大量的无监督数据（运动学生成的轨迹）来提升动作生成器的性能，并减少对配对数据的依赖。

**技术框架**：该方法包含两个主要阶段：1) 动作头预训练阶段：使用无观察数据的运动学轨迹预训练一个通用的动作生成器（动作头）。2) 任务适配阶段：冻结预训练的动作头，并通过特征调制的方式，将任务相关的特征信息融入到动作生成过程中，从而使动作头适应特定的任务。DP-MLP使用MLP替代DP-C的U-Net骨干网络。

**关键创新**：该方法最重要的创新点在于解耦训练的思想，将动作生成与任务特定知识分离。这使得可以利用大量的无监督数据来提升动作生成器的性能，并减少对配对数据的依赖。此外，通过实验验证了动作生成骨干网络在机器人操作中的作用有限，从而提出了更轻量级的DP-MLP模型。

**关键设计**：动作头可以使用各种生成模型，例如扩散模型。特征调制可以通过各种方式实现，例如条件归一化（Conditional Normalization）。论文中使用了DP-CNN和DP-Transformer作为基线模型，并提出了DP-MLP，将U-Net替换为MLP，显著减少了参数量。

## 📊 实验亮点

实验结果表明，解耦训练可以显著提升训练效率，例如DP-C实现了高达41%的加速。此外，DP-MLP通过将DP-C的244M参数U-Net骨干替换为4M参数的MLP，在正常训练下实现了83.9%的更快训练速度，在解耦下实现了89.1%的更快训练速度，同时保持了与DP-C相当的性能。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，例如抓取、放置、装配等。通过解耦训练，可以降低对大量配对数据的依赖，从而加速机器人学习过程，并提升机器人在复杂环境中的泛化能力。该方法还有潜力应用于其他需要生成连续动作序列的任务，例如自动驾驶。

## 📄 摘要（原文）

> Behavior Cloning (BC) is a data-driven supervised learning approach that has gained increasing attention with the success of scaling laws in language and vision domains. Among its implementations in robotic manipulation, Diffusion Policy (DP), with its two variants DP-CNN (DP-C) and DP-Transformer (DP-T), is one of the most effective and widely adopted models, demonstrating the advantages of predicting continuous action sequences. However, both DP and other BC methods remain constrained by the scarcity of paired training data, and the internal mechanisms underlying DP's effectiveness remain insufficiently understood, leading to limited generalization and a lack of principled design in model development. In this work, we propose a decoupled training recipe that leverages nearly cost-free kinematics-generated trajectories as observation-free data to pretrain a general action head (action generator). The pretrained action head is then frozen and adapted to novel tasks through feature modulation. Our experiments demonstrate the feasibility of this approach in both in-distribution and out-of-distribution scenarios. As an additional benefit, decoupling improves training efficiency; for instance, DP-C achieves up to a 41% speedup. Furthermore, the confinement of task-specific knowledge to the conditioning components under decoupling, combined with the near-identical performance of DP-C in both normal and decoupled training, indicates that the action generation backbone plays a limited role in robotic manipulation. Motivated by this observation, we introduce DP-MLP, which replaces the 244M-parameter U-Net backbone of DP-C with only 4M parameters of simple MLP blocks, achieving a 83.9% faster training speed under normal training and 89.1% under decoupling.

