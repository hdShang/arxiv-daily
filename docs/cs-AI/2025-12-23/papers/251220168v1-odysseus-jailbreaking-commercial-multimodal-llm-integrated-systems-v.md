---
layout: default
title: Odysseus: Jailbreaking Commercial Multimodal LLM-integrated Systems via Dual Steganography
---

# Odysseus: Jailbreaking Commercial Multimodal LLM-integrated Systems via Dual Steganography

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20168" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20168v1</a>
  <a href="https://arxiv.org/pdf/2512.20168.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20168v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20168v1', 'Odysseus: Jailbreaking Commercial Multimodal LLM-integrated Systems via Dual Steganography')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Songze Li, Jiameng Cheng, Yiming Li, Xiaojun Jia, Dacheng Tao

**分类**: cs.CR, cs.AI, cs.LG

**发布日期**: 2025-12-23

**备注**: This paper is accepted by Network and Distributed System Security Symposium (NDSS) 2026

---

## 💡 一句话要点

**Odysseus：利用双重隐写术破解商业多模态LLM集成系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `越狱攻击` `隐写术` `安全漏洞` `跨模态安全`

## 📋 核心要点

1. 现有商业MLLM集成系统依赖安全过滤器来防御恶意内容，但这些过滤器假设恶意内容必须显式可见，存在被绕过的风险。
2. Odysseus提出了一种双重隐写术，将恶意查询和响应隐蔽地嵌入到图像中，从而绕过安全过滤器，实现对MLLM集成系统的越狱攻击。
3. 实验表明，Odysseus在多个MLLM集成系统上实现了高达99%的攻击成功率，揭示了现有防御措施的盲点。

## 📝 摘要（中文）

多模态大型语言模型（MLLM）通过整合语言理解与图像等感知模态，构成了现代AI系统，特别是开放和交互环境中智能代理的关键基础。然而，其日益增长的可访问性也带来了滥用的风险，例如生成有害或不安全的内容。为了降低这些风险，通常应用对齐技术使模型行为与人类价值观对齐。尽管如此，最近的研究表明，越狱攻击可以绕过对齐并引出不安全的输出。目前，大多数现有的越狱方法都是为开源模型量身定制的，并且对商业MLLM集成系统的有效性有限，这些系统通常采用额外的过滤器。这些过滤器可以检测和阻止恶意输入和输出内容，从而显著降低越狱威胁。本文揭示了这些安全过滤器的成功在很大程度上依赖于一个关键假设，即恶意内容必须在输入或输出中显式可见。这种假设在MLLM集成系统中失效，攻击者可以利用多种模态来隐藏对抗意图，从而导致现有MLLM集成系统产生虚假的安全感。为了挑战这一假设，我们提出了Odysseus，一种新颖的越狱范例，它引入了双重隐写术，将恶意查询和响应隐蔽地嵌入到看似良性的图像中。在基准数据集上进行的大量实验表明，我们的Odysseus成功地越狱了几个开创性和现实的MLLM集成系统，攻击成功率高达99%。它暴露了现有防御措施中的一个根本盲点，并呼吁重新思考MLLM集成系统中的跨模态安全性。

## 🔬 方法详解

**问题定义**：论文旨在解决商业多模态大型语言模型（MLLM）集成系统中，现有安全过滤器对恶意攻击防御不足的问题。现有方法主要依赖于检测输入或输出中显式可见的恶意内容，但这种假设在多模态场景下容易被绕过。攻击者可以通过隐蔽的方式将恶意信息嵌入到图像等模态中，从而欺骗安全过滤器，导致系统产生不安全或有害的输出。

**核心思路**：论文的核心思路是利用双重隐写术，将恶意查询和响应隐藏在看似无害的图像中。通过这种方式，攻击者可以绕过依赖于显式内容检测的安全过滤器，从而实现对MLLM集成系统的越狱攻击。这种方法的核心在于利用多模态的特性，将恶意信息隐藏在不易被检测的模态中。

**技术框架**：Odysseus框架主要包含以下几个阶段：1) **恶意查询编码**：将恶意查询通过隐写术编码到第一张图像中。2) **MLLM集成系统交互**：将包含恶意查询的图像输入到MLLM集成系统中，系统生成响应。3) **恶意响应编码**：将MLLM的响应（可能包含有害内容）通过隐写术编码到第二张图像中。4) **输出**：输出包含恶意响应的图像。整个流程利用图像作为载体，隐蔽地传递恶意查询和响应，从而绕过安全过滤器的检测。

**关键创新**：论文的关键创新在于提出了双重隐写术的概念，并将其应用于MLLM集成系统的越狱攻击。与传统的越狱方法不同，Odysseus不依赖于显式地操纵文本输入，而是利用图像作为载体，将恶意信息隐藏在不易被检测的模态中。这种方法能够有效地绕过依赖于显式内容检测的安全过滤器，从而实现对MLLM集成系统的攻击。

**关键设计**：论文中，隐写术的选择至关重要，需要选择一种能够保证图像质量，同时又能有效隐藏信息的算法。此外，恶意查询和响应的编码方式也需要精心设计，以避免被安全过滤器检测到。例如，可以使用自适应的隐写算法，根据图像的复杂程度动态调整嵌入强度。同时，可以对恶意信息进行加密或混淆，以进一步提高隐蔽性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20168v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20168v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20168v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Odysseus在多个商业MLLM集成系统上取得了显著的越狱效果，攻击成功率高达99%。这表明现有安全过滤器在多模态场景下存在严重的漏洞，无法有效防御隐蔽的恶意攻击。与传统的基于文本的越狱方法相比，Odysseus能够更有效地绕过安全机制，揭示了多模态AI系统安全性的脆弱性。

## 🎯 应用场景

该研究成果可应用于评估和改进多模态AI系统的安全性。通过模拟Odysseus攻击，开发者可以识别现有防御机制的盲点，并开发更有效的跨模态安全策略。此外，该研究也提醒人们关注多模态AI系统潜在的安全风险，并促进相关安全标准的制定。

## 📄 摘要（原文）

> By integrating language understanding with perceptual modalities such as images, multimodal large language models (MLLMs) constitute a critical substrate for modern AI systems, particularly intelligent agents operating in open and interactive environments. However, their increasing accessibility also raises heightened risks of misuse, such as generating harmful or unsafe content. To mitigate these risks, alignment techniques are commonly applied to align model behavior with human values. Despite these efforts, recent studies have shown that jailbreak attacks can circumvent alignment and elicit unsafe outputs. Currently, most existing jailbreak methods are tailored for open-source models and exhibit limited effectiveness against commercial MLLM-integrated systems, which often employ additional filters. These filters can detect and prevent malicious input and output content, significantly reducing jailbreak threats. In this paper, we reveal that the success of these safety filters heavily relies on a critical assumption that malicious content must be explicitly visible in either the input or the output. This assumption, while often valid for traditional LLM-integrated systems, breaks down in MLLM-integrated systems, where attackers can leverage multiple modalities to conceal adversarial intent, leading to a false sense of security in existing MLLM-integrated systems. To challenge this assumption, we propose Odysseus, a novel jailbreak paradigm that introduces dual steganography to covertly embed malicious queries and responses into benign-looking images. Extensive experiments on benchmark datasets demonstrate that our Odysseus successfully jailbreaks several pioneering and realistic MLLM-integrated systems, achieving up to 99% attack success rate. It exposes a fundamental blind spot in existing defenses, and calls for rethinking cross-modal security in MLLM-integrated systems.

