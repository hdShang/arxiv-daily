---
layout: default
title: The Double Life of Code World Models: Provably Unmasking Malicious Behavior Through Execution Traces
---

# The Double Life of Code World Models: Provably Unmasking Malicious Behavior Through Execution Traces

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13821" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13821</a>
  <a href="https://arxiv.org/pdf/2512.13821.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13821" onclick="toggleFavorite(this, '2512.13821', 'The Double Life of Code World Models: Provably Unmasking Malicious Behavior Through Execution Traces')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Subramanyam Sahoo, Jared Junkin

**分类**: cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出CTVP框架，通过执行轨迹分析揭示代码世界模型中的恶意行为**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `恶意行为检测` `后门攻击` `语义轨道分析` `AI安全`

## 📋 核心要点

1. 现有代码生成模型缺乏有效的恶意行为检测机制，容易被植入后门。
2. CTVP框架通过分析模型在语义等价程序上的执行轨迹一致性，检测恶意行为。
3. 实验证明，CTVP能够有效检测后门，并提出了量化验证成本的ARQ指标。

## 📝 摘要（中文）

大型语言模型（LLM）越来越多地生成代码，而人为监督最少，这引发了对后门注入和恶意行为的严重担忧。我们提出了跨轨迹验证协议（CTVP），这是一种新颖的AI控制框架，通过语义轨道分析来验证不受信任的代码生成模型。CTVP不是直接执行潜在的恶意代码，而是利用模型自身对跨语义等效程序转换的执行轨迹的预测。通过分析这些预测轨迹中的一致性模式，我们检测到指示后门的行为异常。我们的方法引入了对抗鲁棒性商（ARQ），它量化了相对于基线生成的验证计算成本，证明了其随轨道大小呈指数增长。理论分析建立了信息论界限，表明其不可博弈性——由于基本的空间复杂度约束，对抗者无法通过训练来改进。这项工作表明，语义轨道分析为代码生成任务提供了一种可扩展的、具有理论基础的AI控制方法。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在代码生成过程中可能存在的后门注入和恶意行为问题。现有的代码生成模型缺乏有效的验证机制，难以检测和防御潜在的恶意代码，这使得LLM在安全敏感的应用中面临风险。直接执行生成的代码存在安全隐患，而静态分析方法可能无法有效识别复杂的后门逻辑。

**核心思路**：论文的核心思路是利用语义等价的程序转换，构建程序的“语义轨道”，并分析LLM在这些等价程序上的执行轨迹预测的一致性。如果模型存在后门，那么在某些特定的输入条件下，即使程序语义等价，其执行轨迹也会出现异常偏差。通过检测这些偏差，可以有效地识别恶意行为。这种方法避免了直接执行潜在恶意代码的风险，并利用了模型自身的预测能力进行验证。

**技术框架**：CTVP框架包含以下主要模块：1) **程序转换模块**：将原始代码转换为一系列语义等价的程序变体，形成语义轨道。2) **执行轨迹预测模块**：利用待验证的LLM预测每个程序变体的执行轨迹。3) **一致性分析模块**：分析不同程序变体执行轨迹的一致性，检测异常偏差。4) **恶意行为判定模块**：根据偏差程度判断是否存在恶意行为，并计算对抗鲁棒性商（ARQ）来量化验证成本。

**关键创新**：论文的关键创新在于提出了基于语义轨道分析的AI控制框架CTVP，以及对抗鲁棒性商（ARQ）这一量化指标。CTVP通过分析模型自身对语义等价程序执行轨迹的预测，实现了对恶意行为的有效检测，避免了直接执行潜在恶意代码的风险。ARQ则提供了一种量化验证成本的方法，有助于评估不同验证策略的效率。与现有方法相比，CTVP不需要人工标注或预定义的恶意模式，具有更强的通用性和可扩展性。

**关键设计**：CTVP的关键设计包括：1) **语义等价程序转换策略**：选择合适的程序转换方法，确保生成的程序变体在语义上等价，但语法上存在差异，以触发后门行为。2) **执行轨迹预测方法**：利用LLM的预测能力，生成每个程序变体的执行轨迹，例如变量值的变化、函数调用序列等。3) **一致性度量方法**：设计合适的度量方法，量化不同程序变体执行轨迹之间的偏差，例如使用动态时间规整（DTW）或编辑距离等。4) **ARQ计算方法**：定义ARQ为验证成本与基线生成成本之比，其中验证成本包括生成语义轨道和分析执行轨迹所需的计算资源。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13821/experiment_dashboard.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13821/memory_usage.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CTVP能够有效检测代码生成模型中的后门，并量化验证成本。论文提出了对抗鲁棒性商（ARQ），证明了验证成本随轨道大小呈指数增长，表明了该方法的有效性和可扩展性。理论分析建立了信息论界限，表明其不可博弈性，即对抗者无法通过训练来改进。

## 🎯 应用场景

该研究成果可应用于软件安全、AI安全等领域，用于验证代码生成模型的安全性，防止恶意代码的生成和传播。通过CTVP框架，可以提高代码生成模型的可靠性和安全性，降低安全风险。未来，该方法可以扩展到其他AI生成任务，例如文本生成、图像生成等，为AI安全提供更全面的保障。

## 📄 摘要（原文）

> Large language models (LLMs) increasingly generate code with minimal human oversight, raising critical concerns about backdoor injection and malicious behavior. We present Cross-Trace Verification Protocol (CTVP), a novel AI control framework that verifies untrusted code-generating models through semantic orbit analysis. Rather than directly executing potentially malicious code, CTVP leverages the model's own predictions of execution traces across semantically equivalent program transformations. By analyzing consistency patterns in these predicted traces, we detect behavioral anomalies indicative of backdoors. Our approach introduces the Adversarial Robustness Quotient (ARQ), which quantifies the computational cost of verification relative to baseline generation, demonstrating exponential growth with orbit size. Theoretical analysis establishes information-theoretic bounds showing non-gamifiability -- adversaries cannot improve through training due to fundamental space complexity constraints. This work demonstrates that semantic orbit analysis provides a scalable, theoretically grounded approach to AI control for code generation tasks.

