---
layout: default
title: "STaR-Attack: A Spatio-Temporal and Narrative Reasoning Attack Framework for Unified Multimodal Understanding and Generation Models"
---

# STaR-Attack: A Spatio-Temporal and Narrative Reasoning Attack Framework for Unified Multimodal Understanding and Generation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26473" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26473v1</a>
  <a href="https://arxiv.org/pdf/2509.26473.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26473v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26473v1', 'STaR-Attack: A Spatio-Temporal and Narrative Reasoning Attack Framework for Unified Multimodal Understanding and Generation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaoxiong Guo, Tianyi Du, Lijun Li, Yuyao Wu, Jie Li, Jing Shao

**分类**: cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出STaR-Attack框架，揭示并利用统一多模态模型在时空叙事推理上的安全漏洞。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `对抗攻击` `安全漏洞` `时空推理` `叙事生成` `越狱攻击` `生成理解耦合`

## 📋 核心要点

1. 现有攻击方法主要集中于单模态或依赖语义漂移，未能有效利用统一多模态模型(UMMs)中生成与理解耦合的独特漏洞。
2. STaR-Attack通过构建时空叙事场景，将恶意事件隐藏在三幕剧中，利用UMMs的生成和理解能力进行多轮攻击。
3. 实验结果表明，STaR-Attack在攻击成功率上显著优于现有方法，突显了UMMs在安全对齐方面面临的挑战。

## 📝 摘要（中文）

统一多模态理解与生成模型(UMMs)在理解和生成任务中表现出卓越的能力。然而，我们发现UMMs中生成-理解耦合存在漏洞。攻击者可以利用生成功能制作信息丰富的对抗图像，然后利用理解功能单次吸收，我们称之为跨模态生成注入(CMGI)。目前针对恶意指令的攻击方法通常仅限于单一模态，并且依赖于语义漂移的提示重写，未探索UMMs的独特漏洞。我们提出了STaR-Attack，这是第一个多轮越狱攻击框架，它利用UMMs独特的安全弱点，且没有语义漂移。具体来说，我们的方法定义了一个在时空上下文中与目标查询强相关的恶意事件。利用三幕叙事理论，STaR-Attack生成事件前和事件后的场景，同时将恶意事件隐藏为高潮。在执行攻击策略时，前两轮利用UMM的生成能力来生成这些场景的图像。随后，通过利用理解能力，引入基于图像的问题猜测和回答游戏。STaR-Attack将原始恶意问题嵌入到良性候选项中，迫使模型根据叙事上下文选择并回答最相关的问题。大量实验表明，STaR-Attack始终优于现有方法，在Gemini-2.0-Flash上实现了高达93.06%的攻击成功率(ASR)，并超过了最强的先前基线FlipAttack。我们的工作揭示了一个关键但未被充分开发的安全漏洞，并强调了UMMs中安全对齐的必要性。

## 🔬 方法详解

**问题定义**：论文旨在解决统一多模态模型(UMMs)在面对对抗性攻击时存在的安全漏洞问题。现有攻击方法，如基于恶意指令的攻击，通常局限于单一模态，或者依赖于带有语义漂移的提示重写，无法充分利用UMMs生成和理解能力耦合的特性，从而导致攻击效果不佳。

**核心思路**：论文的核心思路是利用UMMs的生成能力，构建一个包含恶意事件的时空叙事场景，并将该恶意事件巧妙地隐藏在叙事的高潮中。通过多轮交互，诱导UMMs在理解叙事上下文的过程中，暴露其安全漏洞。这种方法避免了直接的恶意指令输入，降低了被防御机制检测到的风险。

**技术框架**：STaR-Attack框架主要包含以下几个阶段：1) **叙事场景生成**：利用三幕叙事理论，生成恶意事件发生前和发生后的场景图像。2) **图像生成**：利用UMMs的生成能力，根据叙事场景的描述生成对应的图像。3) **问题猜测与回答**：设计一个基于图像的问题猜测和回答游戏，将原始的恶意问题嵌入到多个良性候选项中。4) **攻击执行**：通过多轮交互，引导UMMs选择并回答与恶意事件相关的最相关问题，从而触发其安全漏洞。

**关键创新**：STaR-Attack的关键创新在于其多轮、时空叙事推理的攻击策略。它不同于以往的单轮或基于语义漂移的攻击方法，而是通过构建一个完整的叙事上下文，将恶意事件隐藏其中，从而更有效地利用了UMMs的生成和理解能力。这种攻击方式更具隐蔽性和欺骗性，能够绕过现有的防御机制。

**关键设计**：在叙事场景生成阶段，需要精心设计事件前、事件后场景的描述，确保它们与恶意事件具有强烈的时空相关性，同时又不会直接暴露恶意事件本身。在问题猜测与回答阶段，需要合理设置良性候选项的数量和内容，避免UMMs轻易识别出恶意问题。此外，还需要调整问题与图像之间的相关性，使得UMMs在理解叙事上下文后，更有可能选择与恶意事件相关的问题。

## 📊 实验亮点

STaR-Attack在Gemini-2.0-Flash上实现了高达93.06%的攻击成功率(ASR)，显著超越了最强的先前基线FlipAttack。实验结果表明，该方法能够有效地利用UMMs的生成和理解能力，揭示其在时空叙事推理方面的安全漏洞。这一发现突显了多模态模型在安全对齐方面面临的严峻挑战，并为未来的研究提供了重要的参考。

## 🎯 应用场景

该研究成果可应用于评估和提升多模态模型的安全性，尤其是在开放域场景下。通过模拟真实的攻击场景，可以帮助开发者发现模型潜在的安全漏洞，并采取相应的防御措施，例如改进模型的安全对齐策略，提高其对对抗性输入的鲁棒性。此外，该研究还可以促进对多模态模型安全性的更深入理解，推动相关领域的发展。

## 📄 摘要（原文）

> Unified Multimodal understanding and generation Models (UMMs) have demonstrated remarkable capabilities in both understanding and generation tasks. However, we identify a vulnerability arising from the generation-understanding coupling in UMMs. The attackers can use the generative function to craft an information-rich adversarial image and then leverage the understanding function to absorb it in a single pass, which we call Cross-Modal Generative Injection (CMGI). Current attack methods on malicious instructions are often limited to a single modality while also relying on prompt rewriting with semantic drift, leaving the unique vulnerabilities of UMMs unexplored. We propose STaR-Attack, the first multi-turn jailbreak attack framework that exploits unique safety weaknesses of UMMs without semantic drift. Specifically, our method defines a malicious event that is strongly correlated with the target query within a spatio-temporal context. Using the three-act narrative theory, STaR-Attack generates the pre-event and the post-event scenes while concealing the malicious event as the hidden climax. When executing the attack strategy, the opening two rounds exploit the UMM's generative ability to produce images for these scenes. Subsequently, an image-based question guessing and answering game is introduced by exploiting the understanding capability. STaR-Attack embeds the original malicious question among benign candidates, forcing the model to select and answer the most relevant one given the narrative context. Extensive experiments show that STaR-Attack consistently surpasses prior approaches, achieving up to 93.06% ASR on Gemini-2.0-Flash and surpasses the strongest prior baseline, FlipAttack. Our work uncovers a critical yet underdeveloped vulnerability and highlights the need for safety alignments in UMMs.

