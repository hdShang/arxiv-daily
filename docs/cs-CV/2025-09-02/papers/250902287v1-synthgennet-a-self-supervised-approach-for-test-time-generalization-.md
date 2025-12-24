---
layout: default
title: "SynthGenNet: a self-supervised approach for test-time generalization using synthetic multi-source domain mixing of street view images"
---

# SynthGenNet: a self-supervised approach for test-time generalization using synthetic multi-source domain mixing of street view images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02287" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02287v1</a>
  <a href="https://arxiv.org/pdf/2509.02287.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02287v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02287v1', 'SynthGenNet: a self-supervised approach for test-time generalization using synthetic multi-source domain mixing of street view images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pushpendra Dhakara, Prachi Chachodhia, Vaibhav Kumar

**分类**: cs.CV

**发布日期**: 2025-09-02

---

## 💡 一句话要点

**SynthGenNet：利用合成街景图像多源域混合实现测试时泛化的自监督方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `自监督学习` `领域泛化` `合成数据` `街景图像` `语义分割`

## 📋 核心要点

1. 城市环境复杂多变，现有场景理解方法泛化能力不足，难以适应真实场景。
2. SynthGenNet通过混合多源合成数据，并结合自监督学习，提升模型在真实场景中的泛化能力。
3. 实验表明，该方法在真实数据集上显著优于现有单源方法，mIoU提升至50%。

## 📝 摘要（中文）

本文提出SynthGenNet，一种自监督的师生架构，旨在利用合成多源图像实现鲁棒的测试时域泛化，解决非结构化城市环境中场景理解和泛化的挑战。核心贡献包括：ClassMix++算法，该算法混合来自不同合成源的带标签数据，同时保持语义完整性，增强模型适应性；Grounded Mask Consistency Loss (GMC)，利用源域真值来提高跨域预测一致性和特征对齐；伪标签引导的对比学习(PLGCL)机制，集成到学生网络中，通过教师网络的迭代知识蒸馏，促进领域不变特征学习。这种自监督策略提高了预测精度，解决了真实世界的可变性，弥合了sim-to-real的域差距，并减少了对带标签目标数据的依赖，即使在复杂的城市区域也是如此。实验结果表明，我们的模型优于依赖单源的state-of-the-art方法，在印度驾驶数据集(IDD)等真实世界数据集上实现了50%的平均交并比(mIoU)值。

## 🔬 方法详解

**问题定义**：现有方法在处理非结构化城市环境中的场景理解任务时，面临着泛化能力不足的问题。这些方法通常依赖于单一来源的数据进行训练，难以适应真实世界中复杂多变的场景布局和光照条件，导致在测试时性能显著下降。因此，如何提升模型在真实场景中的泛化能力，减少对标注数据的依赖，是本文要解决的核心问题。

**核心思路**：本文的核心思路是利用合成数据进行训练，并通过自监督学习的方式，提升模型在真实场景中的泛化能力。具体而言，通过混合多个合成数据源，增加训练数据的多样性，并利用教师-学生网络结构，进行知识蒸馏，从而使学生网络能够学习到领域不变的特征表示。

**技术框架**：SynthGenNet采用师生架构。教师网络利用ClassMix++混合多源合成数据，并使用GMC Loss进行训练。学生网络则通过PLGCL机制，从教师网络中学习领域不变的特征表示。整个框架通过迭代训练，不断提升学生网络的性能。主要模块包括：ClassMix++数据混合模块、GMC Loss计算模块、PLGCL对比学习模块。

**关键创新**：本文的关键创新在于以下三点：1) 提出了ClassMix++算法，能够有效地混合多源合成数据，同时保持语义完整性；2) 提出了GMC Loss，能够利用源域真值来提高跨域预测一致性和特征对齐；3) 提出了PLGCL机制，能够通过对比学习的方式，学习领域不变的特征表示。与现有方法相比，本文的方法能够更好地利用合成数据，提升模型在真实场景中的泛化能力。

**关键设计**：ClassMix++算法的关键在于如何选择混合比例，以保证混合后的数据具有良好的语义一致性。GMC Loss的关键在于如何选择合适的mask，以保证能够有效地约束跨域预测的一致性。PLGCL机制的关键在于如何选择合适的对比样本，以保证能够学习到领域不变的特征表示。此外，教师网络和学生网络的结构选择，以及训练过程中的超参数设置，也会影响最终的性能。

## 📊 实验亮点

SynthGenNet在真实世界数据集（如IDD）上取得了显著的性能提升，mIoU值达到了50%，超越了依赖单源数据的state-of-the-art方法。这表明该方法能够有效地利用合成数据，弥合sim-to-real的域差距，并提升模型在真实场景中的泛化能力。实验结果充分验证了该方法的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、城市规划等领域。通过提升模型在复杂城市环境中的场景理解能力，可以提高自动驾驶系统的安全性，改善机器人导航的准确性，并为城市规划提供更可靠的数据支持。未来，该方法有望扩展到其他领域，例如遥感图像分析、医疗图像诊断等。

## 📄 摘要（原文）

> Unstructured urban environments present unique challenges for scene understanding and generalization due to their complex and diverse layouts. We introduce SynthGenNet, a self-supervised student-teacher architecture designed to enable robust test-time domain generalization using synthetic multi-source imagery. Our contributions include the novel ClassMix++ algorithm, which blends labeled data from various synthetic sources while maintaining semantic integrity, enhancing model adaptability. We further employ Grounded Mask Consistency Loss (GMC), which leverages source ground truth to improve cross-domain prediction consistency and feature alignment. The Pseudo-Label Guided Contrastive Learning (PLGCL) mechanism is integrated into the student network to facilitate domain-invariant feature learning through iterative knowledge distillation from the teacher network. This self-supervised strategy improves prediction accuracy, addresses real-world variability, bridges the sim-to-real domain gap, and reliance on labeled target data, even in complex urban areas. Outcomes show our model outperforms the state-of-the-art (relying on single source) by achieving 50% Mean Intersection-Over-Union (mIoU) value on real-world datasets like Indian Driving Dataset (IDD).

