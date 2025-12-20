---
layout: default
title: Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future
---

# Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16760" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16760v1</a>
  <a href="https://arxiv.org/pdf/2512.16760.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16760v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16760v1', 'Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianshuai Hu, Xiaolu Liu, Song Wang, Yiyao Zhu, Ao Liang, Lingdong Kong, Guoyang Zhao, Zeying Gong, Jun Cen, Zhiyu Huang, Xiaoshuai Hao, Linfeng Li, Hang Song, Xiangtai Li, Jun Ma, Shaojie Shen, Jianke Zhu, Dacheng Tao, Ziwei Liu, Junwei Liang

**分类**: cs.RO

**发布日期**: 2025-12-18

**备注**: Preprint; 40 pages, 7 figures, 9 tables; GitHub at https://github.com/worldbench/awesome-vla-for-ad

---

## 💡 一句话要点

**综述性论文：面向自动驾驶的视觉-语言-动作模型研究进展与未来展望**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `视觉语言动作模型` `多模态学习` `大型语言模型` `端到端学习` `双系统架构` `综述` `决策规划`

## 📋 核心要点

1. 传统自动驾驶依赖“感知-决策-行动”流程，但手工设计组件在复杂场景失效，且感知误差会向下游传播。
2. 视觉-语言-动作（VLA）模型通过结合视觉理解、语言推理和可执行动作，旨在实现更通用和可解释的自动驾驶策略。
3. 论文综述了VLA在自动驾驶中的应用，分析了端到端和双系统两种主要范例，并探讨了未来发展方向。

## 📝 摘要（中文）

自动驾驶长期以来依赖于模块化的“感知-决策-行动”流程，但手工设计的接口和基于规则的组件在复杂或长尾场景中经常失效。其级联设计进一步传播感知误差，降低下游规划和控制的性能。视觉-动作（VA）模型通过学习从视觉输入到动作的直接映射来解决一些局限性，但它们仍然不透明，对分布偏移敏感，并且缺乏结构化推理或指令遵循能力。大型语言模型（LLM）和多模态学习的最新进展推动了视觉-语言-动作（VLA）框架的出现，该框架将感知与基于语言的决策相结合。通过统一视觉理解、语言推理和可操作的输出，VLA为更可解释、更通用和更符合人类习惯的驾驶策略提供了一条途径。本文对新兴的自动驾驶VLA领域进行了结构化描述，追溯了从早期VA方法到现代VLA框架的演变，并将现有方法组织成两种主要范例：端到端VLA，它在单个模型中集成了感知、推理和规划；双系统VLA，它将慢速审议（通过VLM）与快速、安全关键的执行（通过规划器）分开。在这些范例中，我们进一步区分了文本与数值动作生成器以及显式与隐式指导机制等子类。我们还总结了用于评估基于VLA的驾驶系统的代表性数据集和基准，并强调了关键挑战和开放方向，包括鲁棒性、可解释性和指令保真度。总的来说，这项工作旨在为推进人机兼容的自动驾驶系统奠定连贯的基础。

## 🔬 方法详解

**问题定义**：传统自动驾驶系统依赖于模块化的“感知-决策-行动”流程，这些流程通常包含手工设计的接口和规则，在复杂或长尾场景下表现不佳。此外，级联的设计会导致感知误差向下游传播，影响规划和控制的准确性。视觉-动作（VA）模型虽然尝试直接从视觉输入映射到动作，但缺乏可解释性，对数据分布变化敏感，并且难以进行结构化推理和指令遵循。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）和多模态学习的最新进展，构建视觉-语言-动作（VLA）框架，将视觉感知、语言推理和可执行动作统一起来。通过语言作为桥梁，VLA模型能够更好地理解驾驶场景，进行推理和决策，并生成符合人类指令的驾驶行为。这种方法旨在提高自动驾驶系统的通用性、可解释性和人机交互能力。

**技术框架**：论文将现有的VLA方法组织成两种主要范例：端到端VLA和双系统VLA。端到端VLA模型将感知、推理和规划集成到一个单一的模型中，直接从视觉输入生成动作。双系统VLA模型则将慢速审议（通过视觉语言模型VLM）与快速、安全关键的执行（通过规划器）分开，VLM负责高级决策和指令生成，规划器负责低级别的动作控制。在这些范例中，还区分了文本与数值动作生成器以及显式与隐式指导机制等子类。

**关键创新**：论文的主要创新在于对自动驾驶领域的VLA模型进行了系统性的综述和分类，提出了端到端VLA和双系统VLA两种主要范例，并对各种VLA方法的特点和优缺点进行了深入分析。此外，论文还总结了用于评估VLA模型的代表性数据集和基准，并指出了该领域面临的关键挑战和未来发展方向。

**关键设计**：论文本身是一篇综述，因此没有具体的模型设计细节。但是，论文中讨论的VLA模型通常会涉及到以下关键设计：视觉编码器（例如，卷积神经网络或Transformer）用于提取图像特征；语言模型（例如，Transformer）用于处理语言指令和进行推理；动作生成器（例如，神经网络或规划器）用于生成驾驶动作。损失函数的设计通常会涉及到模仿学习、强化学习或两者结合的方法，以训练模型生成符合人类驾驶习惯的动作。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16760v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16760v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16760v1/figures/fig3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文是一篇综述性文章，没有具体的实验结果。但是，论文总结了现有VLA模型在自动驾驶任务中的表现，并指出了该领域面临的关键挑战和未来发展方向。例如，如何提高VLA模型的鲁棒性、可解释性和指令保真度，以及如何利用大规模数据集和预训练模型来提升VLA模型的性能等。

## 🎯 应用场景

该研究对自动驾驶领域具有重要的应用价值。VLA模型能够提升自动驾驶系统的通用性、可解释性和人机交互能力，使其能够更好地适应复杂和动态的驾驶环境，并能够理解和执行人类的指令。未来，VLA模型有望被应用于各种自动驾驶车辆，包括乘用车、卡车和无人配送车等，从而提高交通运输的效率和安全性。

## 📄 摘要（原文）

> Autonomous driving has long relied on modular "Perception-Decision-Action" pipelines, where hand-crafted interfaces and rule-based components often break down in complex or long-tailed scenarios. Their cascaded design further propagates perception errors, degrading downstream planning and control. Vision-Action (VA) models address some limitations by learning direct mappings from visual inputs to actions, but they remain opaque, sensitive to distribution shifts, and lack structured reasoning or instruction-following capabilities. Recent progress in Large Language Models (LLMs) and multimodal learning has motivated the emergence of Vision-Language-Action (VLA) frameworks, which integrate perception with language-grounded decision making. By unifying visual understanding, linguistic reasoning, and actionable outputs, VLAs offer a pathway toward more interpretable, generalizable, and human-aligned driving policies. This work provides a structured characterization of the emerging VLA landscape for autonomous driving. We trace the evolution from early VA approaches to modern VLA frameworks and organize existing methods into two principal paradigms: End-to-End VLA, which integrates perception, reasoning, and planning within a single model, and Dual-System VLA, which separates slow deliberation (via VLMs) from fast, safety-critical execution (via planners). Within these paradigms, we further distinguish subclasses such as textual vs. numerical action generators and explicit vs. implicit guidance mechanisms. We also summarize representative datasets and benchmarks for evaluating VLA-based driving systems and highlight key challenges and open directions, including robustness, interpretability, and instruction fidelity. Overall, this work aims to establish a coherent foundation for advancing human-compatible autonomous driving systems.

