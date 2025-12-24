---
layout: default
title: "GLUE: Global-Local Unified Encoding for Imitation Learning via Key-Patch Tracking"
---

# GLUE: Global-Local Unified Encoding for Imitation Learning via Key-Patch Tracking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23220" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23220v1</a>
  <a href="https://arxiv.org/pdf/2509.23220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23220v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23220v1', 'GLUE: Global-Local Unified Encoding for Imitation Learning via Key-Patch Tracking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ye Chen, Zichen Zhou, Jianyu Dou, Te Cui, Yi Yang, Yufeng Yue

**分类**: cs.RO

**发布日期**: 2025-09-27

**备注**: 8 pages, 5 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://GLUE666.github.io/)

---

## 💡 一句话要点

**提出GLUE，通过关键区域跟踪实现模仿学习的全局-局部统一编码，提升复杂环境下的策略性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `机器人视觉` `全局-局部编码` `关键区域跟踪` `分布外泛化`

## 📋 核心要点

1. 复杂OOD环境下的模仿学习，全局视觉表征易受干扰，导致策略性能下降，局部表征的利用是关键。
2. GLUE通过文本引导机制选择和跟踪关键区域，融合全局和局部特征，引导视觉注意力并保留全局上下文。
3. 实验结果表明，GLUE在模拟和真实环境中均显著优于现有方法，尤其在真实环境泛化能力上提升显著。

## 📝 摘要（中文）

近年来，视觉表征学习在机器人模仿学习中受到了广泛关注。然而，在以杂乱和遮挡为特征的复杂分布外(OOD)环境中，全局视觉表征的注意力可能会被稀释或干扰，导致策略性能下降。任务相关对象的局部表征的不变性提供了一种解决方案。通过有效地利用这些局部表征，可以将训练和测试数据映射到更相似的特征空间，从而缓解协变量偏移问题。因此，我们提出GLUE，一种基于关键区域跟踪的模仿学习全局-局部统一编码框架。GLUE通过采用文本引导机制选择和跟踪关键区域作为关键局部表征。它采用了一种新颖的融合框架，其中全局patch特征查询局部patch以提取关键信息，从而产生相对于全局上下文具有低异质性的细粒度局部特征。这种融合的表征引导机器人的视觉注意力集中于任务相关的对象，并保留精确的全局上下文，从而将训练和测试分布对齐到相似且具有任务信息的特征空间中，最终增强模仿学习策略的鲁棒性。实验表明，GLUE在模拟和真实环境中的各种任务中都取得了强大的性能，在模拟环境中优于最强的基线17.6%，在真实环境中优于36.3%，在真实环境泛化设置中优于58.3%。GLUE的项目网站可在https://GLUE666.github.io/上找到。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂环境中模仿学习策略性能下降的问题，尤其是在存在杂乱、遮挡等干扰因素的分布外(OOD)场景下。现有方法依赖的全局视觉表征容易受到干扰，导致策略泛化能力不足。

**核心思路**：论文的核心思路是利用局部表征的不变性来缓解协变量偏移问题。通过选择和跟踪关键区域（Key-Patches），并将其与全局上下文信息融合，从而使模型能够专注于任务相关的对象，并减少训练和测试数据之间的差异。

**技术框架**：GLUE框架包含以下主要模块：1) **关键区域选择与跟踪**：使用文本引导机制选择和跟踪图像中的关键区域，这些区域被认为是与任务最相关的局部特征。2) **全局-局部特征融合**：设计了一种新颖的融合框架，其中全局patch特征查询局部patch，以提取关键信息，生成细粒度的局部特征。3) **策略学习**：使用融合后的全局-局部特征训练模仿学习策略。

**关键创新**：GLUE的关键创新在于其全局-局部统一编码框架，特别是文本引导的关键区域选择和跟踪机制，以及全局特征查询局部特征的融合方式。这种融合方式能够有效地提取任务相关的局部信息，并将其与全局上下文相结合，从而提高策略的鲁棒性和泛化能力。与现有方法相比，GLUE更关注于提取和利用图像中的关键局部信息，而不是仅仅依赖于全局表征。

**关键设计**：文本引导机制的具体实现细节未知，但推测可能使用了预训练的文本-图像模型（如CLIP）来指导关键区域的选择。融合框架的具体网络结构也未知，但可以推测使用了注意力机制或类似的query-key-value结构来实现全局特征对局部特征的查询。损失函数方面，除了标准的模仿学习损失外，可能还使用了额外的损失函数来鼓励关键区域的稳定跟踪和特征的有效融合。

## 📊 实验亮点

GLUE在模拟和真实环境中的多个任务上都取得了显著的性能提升。在模拟环境中，GLUE优于最强的基线17.6%；在真实环境中，GLUE优于最强的基线36.3%；在真实环境泛化设置中，GLUE优于最强的基线58.3%。这些结果表明，GLUE能够有效地提高模仿学习策略的鲁棒性和泛化能力，尤其是在真实世界的复杂环境中。

## 🎯 应用场景

GLUE框架可应用于各种机器人模仿学习任务，尤其是在复杂、动态和分布外环境中。例如，它可以用于家庭服务机器人、自动驾驶、工业自动化等领域，提高机器人在真实世界中的适应性和鲁棒性。该研究对于提升机器人智能水平，使其能够更好地理解和执行复杂任务具有重要意义。

## 📄 摘要（原文）

> In recent years, visual representation learning has gained widespread attention in robotic imitation learning. However, in complex Out-of-Distribution(OOD) settings characterized by clutter and occlusion, the attention of global visual representations can be diluted or interfered, leading to degraded policy performance. The invariance of local representations for task-relevant objects offers a solution. By efficiently utilizing these local representations, training and testing data can be mapped to a more similar feature space, thereby mitigating the covariate shift problem. Accordingly, we propose GLUE, a global-local unified encoding framework for imitation learning based on key-patch tracking. GLUE selects and tracks key-patches as critical local representations by employing a text-guided mechanism. It features a novel fusion framework where global patch features query local patches to distill essential information, yielding fine-grained local features with low heterogeneity relative to the global context. This fused representation steers the robot's visual attention toward task-relevant objects and preserves precise global context, which together align the training and testing distributions into a similar and task-informative feature space, ultimately enhancing the robustness of the imitation learning policy. Experiments demonstrate that GLUE achieves strong performance across diverse tasks in both simulation and real-world settings, outperforming the strongest baseline by 17.6% in simulation, 36.3% in real-world environments, and 58.3% on real-world generalization settings. The project website of GLUE is available at https://GLUE666.github.io/.

