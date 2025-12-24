---
layout: default
title: "DeGuV: Depth-Guided Visual Reinforcement Learning for Generalization and Interpretability in Manipulation"
---

# DeGuV: Depth-Guided Visual Reinforcement Learning for Generalization and Interpretability in Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04970" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04970v1</a>
  <a href="https://arxiv.org/pdf/2509.04970.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04970v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04970v1', 'DeGuV: Depth-Guided Visual Reinforcement Learning for Generalization and Interpretability in Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tien Pham, Xinyun Chi, Khang Nguyen, Manfred Huber, Angelo Cangelosi

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**DeGuV：深度引导的视觉强化学习，提升操作任务的泛化性和可解释性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉强化学习` `深度学习` `机器人操作` `泛化性` `可解释性` `深度信息` `对比学习` `数据增强`

## 📋 核心要点

1. 视觉强化学习在机器人操作任务中面临泛化性挑战，现有数据增强方法常牺牲样本效率和训练稳定性。
2. DeGuV通过深度信息引导的掩码网络，使智能体关注关键视觉特征，提升数据增强下的鲁棒性。
3. 实验表明，DeGuV在RL-ViGen基准测试中，实现了更好的泛化性和样本效率，并提升了可解释性。

## 📝 摘要（中文）

本文提出了一种名为DeGuV的强化学习框架，旨在提升视觉强化学习在操作任务中的泛化性和样本效率。针对现有方法在数据增强时样本效率低和训练不稳定的问题，DeGuV利用一个可学习的掩码网络，从深度输入中生成掩码，仅保留关键视觉信息，去除不相关的像素。这确保了强化学习智能体专注于重要特征，增强了数据增强下的鲁棒性。此外，DeGuV还结合了对比学习，并稳定了增强下的Q值估计，进一步提高了样本效率和训练稳定性。在RL-ViGen基准测试中，使用Franka Emika机器人对所提出的方法进行了评估，结果表明DeGuV在零样本sim-to-real迁移中优于最先进的方法，并在泛化性和样本效率方面均有提升，同时通过突出显示视觉输入中最相关的区域，提高了可解释性。

## 🔬 方法详解

**问题定义**：视觉强化学习在机器人操作任务中，难以将模拟环境中学习到的策略泛化到真实世界。现有方法依赖大量数据增强，但会降低样本效率，并可能导致训练不稳定，难以平衡泛化性和训练效率。

**核心思路**：DeGuV的核心思路是利用深度信息引导智能体关注场景中的关键特征，忽略不相关信息，从而提高对数据增强的鲁棒性，并提升泛化能力。通过可学习的掩码网络，从深度图像中提取重要区域，减少视觉输入的复杂性，使智能体更容易学习到通用的策略。

**技术框架**：DeGuV框架包含以下几个主要模块：1) 深度掩码网络：用于从深度图像中生成掩码，突出显示重要的视觉区域。2) 强化学习智能体：使用深度掩码后的视觉输入进行策略学习。3) 对比学习模块：用于学习更鲁棒的视觉表征。4) Q值稳定模块：用于稳定数据增强下的Q值估计，提高训练稳定性。整体流程是，首先通过深度掩码网络处理深度图像，然后将掩码后的图像输入到强化学习智能体中进行训练，同时使用对比学习和Q值稳定模块来提高泛化性和训练稳定性。

**关键创新**：DeGuV的关键创新在于利用深度信息引导的视觉特征选择。与传统的数据增强方法不同，DeGuV不是简单地对所有视觉信息进行增强，而是有选择性地保留重要的视觉特征，去除不相关的像素。这种方法可以提高智能体对环境变化的鲁棒性，并减少学习的复杂性。此外，结合对比学习和Q值稳定模块，进一步提高了样本效率和训练稳定性。

**关键设计**：深度掩码网络采用卷积神经网络结构，输入为深度图像，输出为掩码图像。掩码图像与原始RGB图像相乘，得到掩码后的视觉输入。对比学习模块使用InfoNCE损失函数，鼓励相似的视觉表征聚集在一起，不同的视觉表征分散开来。Q值稳定模块通过对Q值进行正则化，防止Q值在数据增强下发生剧烈变化。

## 📊 实验亮点

DeGuV在RL-ViGen基准测试中取得了显著的成果，在零样本sim-to-real迁移任务中，DeGuV的性能优于现有的state-of-the-art方法。具体来说，DeGuV在成功率方面取得了显著提升，并且在样本效率方面也表现出色，能够在更少的训练样本下达到更高的性能。此外，通过可视化深度掩码，可以清晰地看到DeGuV关注的视觉区域，验证了其可解释性。

## 🎯 应用场景

DeGuV在机器人操作任务中具有广泛的应用前景，例如工业自动化、家庭服务机器人、医疗机器人等。通过提高机器人的泛化能力和样本效率，可以降低机器人的部署成本，并使其能够适应更加复杂和动态的环境。此外，DeGuV的可解释性也使其更容易被人类理解和信任，有助于人机协作。

## 📄 摘要（原文）

> Reinforcement learning (RL) agents can learn to solve complex tasks from visual inputs, but generalizing these learned skills to new environments remains a major challenge in RL application, especially robotics. While data augmentation can improve generalization, it often compromises sample efficiency and training stability. This paper introduces DeGuV, an RL framework that enhances both generalization and sample efficiency. In specific, we leverage a learnable masker network that produces a mask from the depth input, preserving only critical visual information while discarding irrelevant pixels. Through this, we ensure that our RL agents focus on essential features, improving robustness under data augmentation. In addition, we incorporate contrastive learning and stabilize Q-value estimation under augmentation to further enhance sample efficiency and training stability. We evaluate our proposed method on the RL-ViGen benchmark using the Franka Emika robot and demonstrate its effectiveness in zero-shot sim-to-real transfer. Our results show that DeGuV outperforms state-of-the-art methods in both generalization and sample efficiency while also improving interpretability by highlighting the most relevant regions in the visual input

