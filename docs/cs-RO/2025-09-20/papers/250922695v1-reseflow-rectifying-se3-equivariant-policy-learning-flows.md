---
layout: default
title: "ReSeFlow: Rectifying SE(3)-Equivariant Policy Learning Flows"
---

# ReSeFlow: Rectifying SE(3)-Equivariant Policy Learning Flows

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22695" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22695v1</a>
  <a href="https://arxiv.org/pdf/2509.22695.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22695v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22695v1', 'ReSeFlow: Rectifying SE(3)-Equivariant Policy Learning Flows')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhitao Wang, Yanke Wang, Jiangtao Wen, Roberto Horowitz, Yuxing Han

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-20

**备注**: This work was submitted to 2026 IEEE International Conference on Robotics & Automation

---

## 💡 一句话要点

**提出ReSeFlow，一种快速且SE(3)等变的策略学习方法，提升机器人操作效率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `策略学习` `SE(3)等变性` `扩散模型` `校正流` `轨迹生成` `数据高效` `快速推理`

## 📋 核心要点

1. 现有SE(3)等变扩散模型在机器人操作策略学习中表现出数据高效性，但推理时间成本较高，限制了其应用。
2. ReSeFlow通过引入校正流到SE(3)扩散模型中，实现快速、测地一致且计算量小的策略生成，提升推理效率。
3. 实验表明，ReSeFlow仅需一步推理即可在绘画和旋转三角形任务中显著优于需要100步推理的基线方法。

## 📝 摘要（中文）

本文提出ReSeFlow，一种校正SE(3)等变策略学习流，旨在解决非结构化环境中机器人操作任务中，长时程轨迹策略生成的需求。该方法利用SE(3)等变扩散模型的优势，实现数据高效性，并借鉴校正流的推理效率，提供快速、测地一致、计算量最小的策略生成。ReSeFlow的关键在于其所有组件都采用SE(3)等变网络，以保持旋转和平移对称性，从而在刚体运动下实现鲁棒的泛化。在模拟基准测试中，ReSeFlow仅需一步推理即可实现比基线方法更好的性能和更低的测地距离，在绘画任务中误差降低高达48.5%，在旋转三角形任务中误差降低21.9%（基线方法为100步推理）。该方法结合了SE(3)等变性和校正流的优点，推动了生成策略学习模型在实际应用中的数据和推理效率。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人操作中，尤其是在非结构化环境中，生成鲁棒且长时程轨迹策略的问题。现有基于SE(3)等变扩散模型的策略学习方法虽然数据效率高，但推理速度慢，难以满足实时性要求。

**核心思路**：论文的核心思路是将校正流（Rectified Flow）的思想引入到SE(3)等变扩散模型中。校正流通过学习一个直接的映射关系，减少了迭代推理的步骤，从而显著提升推理速度。结合SE(3)等变性，保证了模型在刚体变换下的不变性，增强了泛化能力。

**技术框架**：ReSeFlow的整体框架包含两个主要部分：SE(3)等变网络和校正流。SE(3)等变网络用于提取感知观测的特征，并保证模型对旋转和平移的等变性。校正流则学习从噪声空间到策略空间的直接映射，从而实现快速策略生成。训练过程中，模型学习如何将噪声数据“校正”为有效的策略轨迹。

**关键创新**：ReSeFlow的关键创新在于将校正流的思想与SE(3)等变扩散模型相结合。与传统的扩散模型需要多次迭代采样不同，ReSeFlow通过学习一个单步映射，极大地提高了推理速度。同时，SE(3)等变性的引入保证了模型在刚体变换下的鲁棒性，使其能够更好地适应真实世界的复杂环境。

**关键设计**：ReSeFlow的关键设计包括：1) 使用SE(3)等变卷积神经网络来提取特征，保证模型对旋转和平移的等变性；2) 设计合适的损失函数，鼓励校正流学习到平滑且测地一致的映射；3) 采用特定的网络结构，例如残差连接等，来提高模型的训练稳定性和性能。

## 📊 实验亮点

ReSeFlow在模拟实验中表现出色。在绘画任务中，ReSeFlow仅需一步推理即可达到比基线方法（100步推理）低48.5%的误差。在旋转三角形任务中，误差降低了21.9%。这些结果表明，ReSeFlow在保证性能的同时，显著提高了推理速度，验证了其有效性。

## 🎯 应用场景

ReSeFlow在机器人操作领域具有广泛的应用前景，例如自动驾驶、工业自动化、医疗机器人等。它可以用于生成机器人抓取、装配、导航等任务的策略，提高机器人的自主性和适应性。该方法的高效性和鲁棒性使其能够应用于实时性要求高的场景，并有望推动机器人技术在实际应用中的普及。

## 📄 摘要（原文）

> Robotic manipulation in unstructured environments requires the generation of robust and long-horizon trajectory-level policy with conditions of perceptual observations and benefits from the advantages of SE(3)-equivariant diffusion models that are data-efficient. However, these models suffer from the inference time costs. Inspired by the inference efficiency of rectified flows, we introduce the rectification to the SE(3)-diffusion models and propose the ReSeFlow, i.e., Rectifying SE(3)-Equivariant Policy Learning Flows, providing fast, geodesic-consistent, least-computational policy generation. Crucially, both components employ SE(3)-equivariant networks to preserve rotational and translational symmetry, enabling robust generalization under rigid-body motions. With the verification on the simulated benchmarks, we find that the proposed ReSeFlow with only one inference step can achieve better performance with lower geodesic distance than the baseline methods, achieving up to a 48.5% error reduction on the painting task and a 21.9% reduction on the rotating triangle task compared to the baseline's 100-step inference. This method takes advantages of both SE(3) equivariance and rectified flow and puts it forward for the real-world application of generative policy learning models with the data and inference efficiency.

