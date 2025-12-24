---
layout: default
title: Identifying Appropriately-Sized Services with Deep Reinforcement Learning
---

# Identifying Appropriately-Sized Services with Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20381" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20381v1</a>
  <a href="https://arxiv.org/pdf/2512.20381.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20381v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20381v1', 'Identifying Appropriately-Sized Services with Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Syeda Tasnim Fabiha, Saad Shafiq, Wesley Klewerton Guez Assunção, Nenad Medvidović

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-23

**备注**: 22 pages, 6 figures

---

## 💡 一句话要点

**提出Rake，利用深度强化学习从实现工件中识别合适大小的服务。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `服务分解` `深度强化学习` `微服务架构` `遗留系统现代化` `模块化质量`

## 📋 核心要点

1. 现有服务分解方法依赖于文档、人员访问或先验知识，在实际场景中受限。
2. Rake利用深度强化学习，直接从代码和文档中学习服务分解策略。
3. 实验表明，Rake在模块化质量和业务能力对齐方面优于现有技术。

## 📝 摘要（中文）

面向服务架构(SBA)作为一种现代化遗留系统的方法，在工业界和学术界受到了广泛关注。它指的是一种设计风格，使系统能够被开发为小型、松散耦合和自治的组件（服务）套件，这些组件封装了功能并通过语言无关的API进行通信。然而，定义能够捕获系统功能内聚子集的适当大小的服务仍然具有挑战性。现有工作通常依赖于文档的可用性、对项目人员的访问或对目标服务数量的先验知识，这些假设在许多实际场景中并不成立。我们的工作使用基于深度强化学习的方法来解决这些限制，直接从实现工件中识别适当大小的服务。我们提出Rake，一种基于强化学习的技术，它利用可用的系统文档和源代码来指导实现方法级别的服务分解。Rake不需要特定的文档或对项目人员的访问，并且是语言无关的。它还支持可定制的目标函数，该函数平衡模块化质量和业务能力对齐，即服务覆盖目标业务能力的程度。我们将Rake应用于四个开源遗留项目，并将其与两种最先进的技术进行了比较。平均而言，Rake实现了高7-14%的模块化质量和18-22%的业务能力对齐。我们的结果进一步表明，仅针对业务上下文进行优化会降低紧密耦合系统中的分解质量，突出了平衡目标的需求。

## 🔬 方法详解

**问题定义**：论文旨在解决服务型架构中服务粒度划分的问题。现有方法依赖于人工经验或特定文档，难以自动化且效果受限。痛点在于如何从代码和文档等实现工件中自动识别合适大小的服务，同时兼顾模块化质量和业务能力对齐。

**核心思路**：论文的核心思路是将服务分解问题建模为强化学习任务。通过训练智能体，使其能够根据代码和文档信息，逐步决策如何将方法聚合成服务。这种方法无需人工干预，能够自动学习最优的服务分解策略。

**技术框架**：Rake的技术框架主要包括以下几个模块：1) 环境：模拟服务分解过程，包括代码和文档信息；2) 智能体：基于深度神经网络，负责决策如何将方法聚合成服务；3) 奖励函数：评估服务分解的质量，包括模块化质量和业务能力对齐；4) 训练过程：通过强化学习算法，不断优化智能体的策略。

**关键创新**：Rake的关键创新在于：1) 将服务分解问题建模为强化学习任务，实现了自动化服务分解；2) 提出了可定制的目标函数，能够平衡模块化质量和业务能力对齐；3) 无需特定文档或人员访问，具有良好的通用性。

**关键设计**：Rake的关键设计包括：1) 使用深度神经网络作为智能体的策略网络，能够处理复杂的代码和文档信息；2) 设计了合适的奖励函数，鼓励智能体生成高质量的服务分解方案；3) 采用了Actor-Critic算法进行训练，提高了训练效率和稳定性。具体的网络结构、损失函数和参数设置在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20381v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20381v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20381v1/figures/Approach-ODG.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Rake在四个开源遗留项目上进行了评估，并与两种最先进的技术进行了比较。实验结果表明，Rake在模块化质量方面平均提高了7-14%，在业务能力对齐方面平均提高了18-22%。这些结果表明，Rake能够有效地识别合适大小的服务，并优于现有技术。

## 🎯 应用场景

Rake可应用于遗留系统的现代化改造、微服务架构设计等领域。通过自动化服务分解，可以降低系统重构的成本和风险，提高系统的可维护性和可扩展性。未来，该技术可进一步应用于云原生应用开发、DevOps等领域，提升软件开发的效率和质量。

## 📄 摘要（原文）

> Service-based architecture (SBA) has gained attention in industry and academia as a means to modernize legacy systems. It refers to a design style that enables systems to be developed as suites of small, loosely coupled, and autonomous components (services) that encapsulate functionality and communicate via language-agnostic APIs. However, defining appropriately sized services that capture cohesive subsets of system functionality remains challenging. Existing work often relies on the availability of documentation, access to project personnel, or a priori knowledge of the target number of services, assumptions that do not hold in many real-world scenarios. Our work addresses these limitations using a deep reinforcement learning-based approach to identify appropriately sized services directly from implementation artifacts. We present Rake, a reinforcement learning-based technique that leverages available system documentation and source code to guide service decomposition at the level of implementation methods. Rake does not require specific documentation or access to project personnel and is language-agnostic. It also supports a customizable objective function that balances modularization quality and business capability alignment, i.e., the degree to which a service covers the targeted business capability. We applied Rake to four open-source legacy projects and compared it with two state-of-the-art techniques. On average, Rake achieved 7-14 percent higher modularization quality and 18-22 percent stronger business capability alignment. Our results further show that optimizing solely for business context can degrade decomposition quality in tightly coupled systems, highlighting the need for balanced objectives.

