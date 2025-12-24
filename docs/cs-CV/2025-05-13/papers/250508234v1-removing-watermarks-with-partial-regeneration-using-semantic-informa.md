---
layout: default
title: Removing Watermarks with Partial Regeneration using Semantic Information
---

# Removing Watermarks with Partial Regeneration using Semantic Information

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08234" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08234v1</a>
  <a href="https://arxiv.org/pdf/2505.08234.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08234v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08234v1', 'Removing Watermarks with Partial Regeneration using Semantic Information')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Krti Tallam, John Kevin Cava, Caleb Geniesse, N. Benjamin Erichson, Michael W. Mahoney

**分类**: cs.CV, cs.AI, cs.CR

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出SemanticRegen以解决水印防护脆弱性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `水印去除` `语义信息` `图像处理` `扩散模型` `视觉-语言模型` `版权保护` `适应性对手`

## 📋 核心要点

1. 现有的水印防护方法在面对适应性对手时表现出脆弱性，尤其是在语义水印方面。
2. 本文提出的SemanticRegen方法通过三阶段流程，利用视觉-语言模型和扩散模型，有效去除水印而不改变图像内容。
3. 在1000个提示的实验中，SemanticRegen成功击败了TreeRing水印，并在其他水印系统中显著降低了比特准确率，同时保持高感知质量。

## 📝 摘要（中文）

随着AI生成图像的普及，隐形水印成为版权和来源保护的主要手段。最新的水印方案嵌入语义信号，旨在抵御常见图像处理，但其对适应性对手的真正鲁棒性尚未得到充分探索。本文揭示了一种未报告的脆弱性，并提出了SemanticRegen，这是一种三阶段的无标签攻击方法，能够在保持图像表面意义不变的情况下，去除最先进的语义和隐形水印。我们的管道通过视觉-语言模型获取细粒度标题，使用零样本分割提取前景掩码，并通过LLM引导的扩散模型仅对背景进行修复，从而保留显著对象和风格线索。实验结果表明，SemanticRegen在四种水印系统上表现出色，突显了当前水印防御与适应性语义对手能力之间的紧迫差距。

## 🔬 方法详解

**问题定义**：本文旨在解决当前水印防护方法在面对适应性对手时的脆弱性，尤其是针对嵌入语义信号的水印。现有方法在图像处理后仍可能被攻击者轻易去除，导致版权保护失效。

**核心思路**：SemanticRegen的核心思路是通过三阶段的无标签攻击流程，利用视觉-语言模型生成细粒度描述，提取前景并仅对背景进行修复，从而在去除水印的同时保留图像的主要内容和风格。

**技术框架**：整体架构包括三个主要模块：第一阶段使用视觉-语言模型生成图像的细粒度标题；第二阶段通过零样本分割提取前景掩码；第三阶段利用LLM引导的扩散模型对背景进行修复。

**关键创新**：本文的主要创新在于引入了masked SSIM（mSSIM）作为评估指标，量化前景区域的保真度，并且SemanticRegen是唯一成功击败TreeRing水印的方法，展示了其在水印去除上的有效性。

**关键设计**：在技术细节上，SemanticRegen采用了LLM引导的扩散模型进行背景修复，确保了显著对象和风格线索的保留，同时在实验中表现出高达12%的mSSIM提升，相较于以往的扩散攻击者具有明显优势。

## 📊 实验亮点

实验结果显示，SemanticRegen在1000个提示的测试中成功击败了TreeRing水印，并将其他水印系统的比特准确率降低至0.75以下，同时保持高感知质量，masked SSIM达到0.94 +/- 0.01，显示出其在水印去除方面的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括数字版权管理、图像内容保护以及AI生成内容的安全性。随着AI技术的不断发展，保护创作者的权益和确保内容的真实性变得愈发重要。未来，SemanticRegen可能推动更为鲁棒的水印算法的开发，以抵御新型的内容保护攻击。

## 📄 摘要（原文）

> As AI-generated imagery becomes ubiquitous, invisible watermarks have emerged as a primary line of defense for copyright and provenance. The newest watermarking schemes embed semantic signals - content-aware patterns that are designed to survive common image manipulations - yet their true robustness against adaptive adversaries remains under-explored. We expose a previously unreported vulnerability and introduce SemanticRegen, a three-stage, label-free attack that erases state-of-the-art semantic and invisible watermarks while leaving an image's apparent meaning intact. Our pipeline (i) uses a vision-language model to obtain fine-grained captions, (ii) extracts foreground masks with zero-shot segmentation, and (iii) inpaints only the background via an LLM-guided diffusion model, thereby preserving salient objects and style cues. Evaluated on 1,000 prompts across four watermarking systems - TreeRing, StegaStamp, StableSig, and DWT/DCT - SemanticRegen is the only method to defeat the semantic TreeRing watermark (p = 0.10 > 0.05) and reduces bit-accuracy below 0.75 for the remaining schemes, all while maintaining high perceptual quality (masked SSIM = 0.94 +/- 0.01). We further introduce masked SSIM (mSSIM) to quantify fidelity within foreground regions, showing that our attack achieves up to 12 percent higher mSSIM than prior diffusion-based attackers. These results highlight an urgent gap between current watermark defenses and the capabilities of adaptive, semantics-aware adversaries, underscoring the need for watermarking algorithms that are resilient to content-preserving regenerative attacks.

