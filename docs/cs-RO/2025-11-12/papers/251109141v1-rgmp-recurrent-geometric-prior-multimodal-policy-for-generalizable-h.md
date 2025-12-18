---
layout: default
title: RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation
---

# RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09141" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09141v1</a>
  <a href="https://arxiv.org/pdf/2511.09141.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09141v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.09141v1', 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuetao Li, Wenke Huang, Nengyuan Pan, Kaiyan Zhao, Songhua Yang, Yiming Wang, Mengde Li, Mang Ye, Jifeng Xuan, Miao Li

**分类**: cs.RO

**发布日期**: 2025-11-12

**期刊**: Proceedings of the AAAI conference on artificial intelligence, 2026

---

## 💡 一句话要点

**提出RGMP，融合几何先验与递归高斯过程，提升人形机器人操作的泛化性和数据效率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `人形机器人操作` `几何先验` `多模态策略` `递归高斯过程` `数据高效` `视觉运动控制` `泛化能力`

## 📋 核心要点

1. 现有数据驱动方法依赖大量训练数据，忽略了几何推理，且机器人-目标关系建模效率低，导致泛化性差。
2. RGMP框架融合几何语义技能推理与数据高效视觉运动控制，提升在未见场景下的泛化能力。
3. 实验表明，RGMP在泛化测试中成功率达87%，数据效率比现有方法提升5倍，验证了其优越性。

## 📝 摘要（中文）

本文提出了一种名为递归几何先验多模态策略（RGMP）的端到端框架，旨在统一几何语义技能推理与数据高效的视觉运动控制，从而提升人形机器人的操作能力。该方法通过几何先验技能选择器，将几何归纳偏置注入视觉语言模型，为未见场景生成自适应技能序列。同时，引入自适应递归高斯网络，将机器人-目标交互参数化为紧凑的高斯过程层级结构，递归编码多尺度空间关系，实现数据高效的灵巧运动合成。在人形机器人和桌面双臂机器人上的评估表明，RGMP在泛化测试中实现了87%的任务成功率，并且比最先进的模型提高了5倍的数据效率。这突显了其由几何语义推理和递归高斯自适应所支持的卓越跨域泛化能力。

## 🔬 方法详解

**问题定义**：现有的人形机器人操作方法严重依赖大量的数据驱动，这导致了两个主要问题：一是忽略了在未见场景中的几何推理能力，二是训练数据中机器人与目标关系的建模效率低下，造成了训练资源的浪费。因此，如何提升人形机器人在新场景下的泛化能力，并降低对大量训练数据的依赖，是本文要解决的核心问题。

**核心思路**：RGMP的核心思路是将几何先验知识融入到多模态策略中，从而提升模型对场景的理解和推理能力。具体来说，通过几何先验技能选择器来引导视觉语言模型，使其能够根据场景的几何特征选择合适的技能序列。同时，利用自适应递归高斯网络来高效地建模机器人与目标之间的复杂关系，从而实现数据高效的运动合成。

**技术框架**：RGMP框架主要包含两个核心模块：几何先验技能选择器（Geometric-prior Skill Selector）和自适应递归高斯网络（Adaptive Recursive Gaussian Network）。首先，几何先验技能选择器利用视觉语言模型提取场景的语义信息，并结合几何先验知识选择合适的技能序列。然后，自适应递归高斯网络根据选择的技能序列，递归地编码多尺度空间关系，生成机器人的运动轨迹。整个框架是一个端到端的训练流程，可以直接从视觉输入到运动输出。

**关键创新**：RGMP的关键创新在于将几何先验知识融入到多模态策略中，并利用递归高斯网络高效地建模机器人与目标之间的关系。与现有方法相比，RGMP不需要大量的训练数据，并且能够更好地泛化到未见场景。此外，自适应递归高斯网络能够以紧凑的方式表示复杂的空间关系，从而提高了运动合成的效率。

**关键设计**：几何先验技能选择器通过引入几何归纳偏置来引导视觉语言模型，使其能够更好地理解场景的几何特征。自适应递归高斯网络则通过递归地编码多尺度空间关系，来高效地建模机器人与目标之间的复杂关系。具体的网络结构和损失函数等技术细节在论文中有详细的描述。

## 📊 实验亮点

RGMP框架在人形机器人和桌面双臂机器人上进行了评估，结果表明其在泛化测试中实现了87%的任务成功率，并且比最先进的模型提高了5倍的数据效率。这些结果表明，RGMP框架具有优越的跨域泛化能力和数据效率，能够有效地解决现有方法的局限性。

## 🎯 应用场景

RGMP框架具有广泛的应用前景，可应用于家庭服务机器人、工业自动化、医疗康复等领域。该技术能够使人形机器人在复杂和动态的环境中执行各种任务，例如物品抓取、装配、清洁等。通过提升机器人的泛化能力和数据效率，可以降低机器人的部署成本，并使其能够更好地适应不同的应用场景。

## 📄 摘要（原文）

> Humanoid robots exhibit significant potential in executing diverse human-level skills. However, current research predominantly relies on data-driven approaches that necessitate extensive training datasets to achieve robust multimodal decision-making capabilities and generalizable visuomotor control. These methods raise concerns due to the neglect of geometric reasoning in unseen scenarios and the inefficient modeling of robot-target relationships within the training data, resulting in significant waste of training resources. To address these limitations, we present the Recurrent Geometric-prior Multimodal Policy (RGMP), an end-to-end framework that unifies geometric-semantic skill reasoning with data-efficient visuomotor control. For perception capabilities, we propose the Geometric-prior Skill Selector, which infuses geometric inductive biases into a vision language model, producing adaptive skill sequences for unseen scenes with minimal spatial common sense tuning. To achieve data-efficient robotic motion synthesis, we introduce the Adaptive Recursive Gaussian Network, which parameterizes robot-object interactions as a compact hierarchy of Gaussian processes that recursively encode multi-scale spatial relationships, yielding dexterous, data-efficient motion synthesis even from sparse demonstrations. Evaluated on both our humanoid robot and desktop dual-arm robot, the RGMP framework achieves 87% task success in generalization tests and exhibits 5x greater data efficiency than the state-of-the-art model. This performance underscores its superior cross-domain generalization, enabled by geometric-semantic reasoning and recursive-Gaussion adaptation.

