---
layout: default
title: "Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future"
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

**关键词**: `自动驾驶` `视觉-语言-动作模型` `大型语言模型` `多模态学习` `端到端学习`

## 📋 核心要点

1. 传统自动驾驶依赖“感知-决策-行动”流程，但存在手工设计接口失效、感知误差传播等问题，限制了其在复杂场景下的应用。
2. 视觉-语言-动作（VLA）模型通过整合视觉理解、语言推理和动作输出，旨在实现更可解释、通用且符合人类习惯的自动驾驶策略。
3. 论文对VLA领域进行了系统性综述，总结了现有方法、数据集和基准，并指出了鲁棒性、可解释性和指令保真度等关键挑战。

## 📝 摘要（中文）

自动驾驶长期以来依赖于模块化的“感知-决策-行动”流程，但手工设计的接口和基于规则的组件在复杂或长尾场景中经常失效。其级联设计进一步传播感知误差，降低下游规划和控制的性能。视觉-动作（VA）模型通过学习从视觉输入到动作的直接映射来解决一些局限性，但它们仍然不透明，对分布偏移敏感，并且缺乏结构化推理或指令遵循能力。大型语言模型（LLM）和多模态学习的最新进展推动了视觉-语言-动作（VLA）框架的出现，该框架将感知与基于语言的决策相结合。通过统一视觉理解、语言推理和可操作的输出，VLA为更可解释、更通用和更符合人类习惯的驾驶策略提供了一条途径。本文对新兴的自动驾驶VLA领域进行了结构化描述，追溯了从早期VA方法到现代VLA框架的演变，并将现有方法组织成两种主要范例：端到端VLA，它在单个模型中集成了感知、推理和规划；以及双系统VLA，它将慢速审议（通过VLM）与快速、安全关键的执行（通过规划器）分开。在这些范例中，我们进一步区分了文本与数值动作生成器以及显式与隐式指导机制等子类。我们还总结了用于评估基于VLA的驾驶系统的代表性数据集和基准，并强调了关键挑战和开放方向，包括鲁棒性、可解释性和指令保真度。总的来说，这项工作旨在为推进与人类兼容的自动驾驶系统奠定连贯的基础。

## 🔬 方法详解

**问题定义**：传统自动驾驶系统依赖于模块化的“感知-决策-行动”流程，各个模块之间通过手工设计的接口连接。这种设计在复杂或长尾场景下容易失效，并且感知模块的误差会逐级传递，影响下游的决策和控制。此外，早期的视觉-动作(VA)模型虽然能够直接从视觉输入预测动作，但缺乏可解释性和泛化能力，难以应对分布偏移。

**核心思路**：论文的核心思路是总结和分析近年来兴起的视觉-语言-动作（VLA）模型在自动驾驶领域的应用。VLA模型通过引入大型语言模型（LLM）进行语言推理，从而将视觉感知、语言理解和动作执行统一起来，旨在提高自动驾驶系统的可解释性、泛化能力和指令遵循能力。论文将现有VLA模型分为端到端VLA和双系统VLA两大类，并对各类方法进行了详细的分析和比较。

**技术框架**：论文将现有的VLA模型分为以下两类：
1. **端到端VLA**：该类模型将感知、推理和规划集成到一个统一的模型中，直接从视觉输入和语言指令预测车辆的动作。这类模型通常采用Transformer架构，利用注意力机制实现多模态信息的融合。
2. **双系统VLA**：该类模型将决策过程分为两个阶段：慢速审议和快速执行。慢速审议阶段由视觉语言模型（VLM）负责，根据视觉输入和语言指令生成高级别的规划。快速执行阶段由传统的规划器或控制器负责，根据高级别的规划生成具体的车辆控制指令。

**关键创新**：论文的主要创新在于对自动驾驶领域的VLA模型进行了系统的分类和总结，并指出了该领域面临的关键挑战和未来发展方向。论文提出的分类框架（端到端VLA和双系统VLA）有助于研究人员更好地理解和比较不同的VLA模型。此外，论文还总结了用于评估VLA模型的代表性数据集和基准，为未来的研究提供了参考。

**关键设计**：论文没有提出新的模型或算法，而是一篇综述性文章，因此没有具体的参数设置、损失函数或网络结构等技术细节。但是，论文对现有VLA模型的技术细节进行了详细的描述，包括不同模型的架构、训练方法和评估指标等。

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

该论文是一篇综述性文章，没有具体的实验结果。但是，论文总结了现有VLA模型在自动驾驶数据集上的性能表现，并指出了不同模型的优缺点。例如，一些端到端VLA模型在特定场景下取得了较好的性能，但泛化能力较差；而双系统VLA模型则在安全性和可解释性方面具有优势。

## 🎯 应用场景

该研究对自动驾驶领域具有重要的应用价值。VLA模型有望提高自动驾驶系统的安全性、可靠性和智能化水平，使其能够更好地适应复杂多变的交通环境。此外，VLA模型还可以实现更自然的人机交互，例如通过语音指令控制车辆的行驶。

## 📄 摘要（原文）

> Autonomous driving has long relied on modular "Perception-Decision-Action" pipelines, where hand-crafted interfaces and rule-based components often break down in complex or long-tailed scenarios. Their cascaded design further propagates perception errors, degrading downstream planning and control. Vision-Action (VA) models address some limitations by learning direct mappings from visual inputs to actions, but they remain opaque, sensitive to distribution shifts, and lack structured reasoning or instruction-following capabilities. Recent progress in Large Language Models (LLMs) and multimodal learning has motivated the emergence of Vision-Language-Action (VLA) frameworks, which integrate perception with language-grounded decision making. By unifying visual understanding, linguistic reasoning, and actionable outputs, VLAs offer a pathway toward more interpretable, generalizable, and human-aligned driving policies. This work provides a structured characterization of the emerging VLA landscape for autonomous driving. We trace the evolution from early VA approaches to modern VLA frameworks and organize existing methods into two principal paradigms: End-to-End VLA, which integrates perception, reasoning, and planning within a single model, and Dual-System VLA, which separates slow deliberation (via VLMs) from fast, safety-critical execution (via planners). Within these paradigms, we further distinguish subclasses such as textual vs. numerical action generators and explicit vs. implicit guidance mechanisms. We also summarize representative datasets and benchmarks for evaluating VLA-based driving systems and highlight key challenges and open directions, including robustness, interpretability, and instruction fidelity. Overall, this work aims to establish a coherent foundation for advancing human-compatible autonomous driving systems.

