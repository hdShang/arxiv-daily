---
layout: default
title: "PhishKey: A Novel Centroid-Based Approach for Enhanced Phishing Detection Using Adaptive HTML Component Extraction"
---

# PhishKey: A Novel Centroid-Based Approach for Enhanced Phishing Detection Using Adaptive HTML Component Extraction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21106" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21106v1</a>
  <a href="https://arxiv.org/pdf/2506.21106.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21106v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21106v1', 'PhishKey: A Novel Centroid-Based Approach for Enhanced Phishing Detection Using Adaptive HTML Component Extraction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Felipe Castaño, Eduardo Fidalgo, Enrique Alegre, Rocio Alaiz-Rodríguez, Raul Orduna, Francesco Zola

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出PhishKey以解决网络钓鱼检测的适应性与效率问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `网络钓鱼检测` `卷积神经网络` `特征提取` `对抗性攻击` `自动化技术`

## 📋 核心要点

1. 现有的网络钓鱼检测方法在适应性和鲁棒性方面存在不足，难以应对快速演变的攻击方式。
2. PhishKey通过结合字符级处理和卷积神经网络，采用基于质心的提取器来自动提取特征，提升检测效果。
3. 在四个数据集上的实验结果显示，PhishKey的F1分数高达98.70%，并对对抗性攻击具有良好的抵抗能力。

## 📝 摘要（中文）

网络钓鱼攻击对网络安全构成了重大威胁，迅速演变以绕过检测机制并利用人类的脆弱性。本文提出了PhishKey，旨在解决适应性、鲁棒性和效率的挑战。PhishKey是一种新颖的网络钓鱼检测方法，利用自动特征提取技术结合混合来源。它将字符级处理与卷积神经网络（CNN）相结合进行URL分类，并采用基于质心的关键组件钓鱼提取器（CAPE）在词级别处理HTML内容。CAPE减少了噪声，确保完整样本处理，避免对输入数据进行裁剪操作。两个模块的预测通过软投票集成，以实现更准确和可靠的分类。在四个最先进的数据集上的实验评估表明，PhishKey的有效性，F1分数高达98.70%，并对注入攻击等对抗性操作表现出强大的抵抗力，性能下降极小。

## 🔬 方法详解

**问题定义**：本文旨在解决网络钓鱼检测中的适应性和效率问题。现有方法往往难以应对快速变化的攻击模式，导致检测效果不佳。

**核心思路**：PhishKey的核心思想是通过自动特征提取结合混合来源，利用字符级处理和卷积神经网络（CNN）进行URL分类，同时采用基于质心的关键组件提取器（CAPE）处理HTML内容，以提高检测的准确性和鲁棒性。

**技术框架**：PhishKey的整体架构包括两个主要模块：一个是基于CNN的URL分类器，另一个是CAPE模块用于HTML内容的提取。两个模块的预测结果通过软投票集成，形成最终的分类结果。

**关键创新**：PhishKey的关键创新在于引入了CAPE模块，该模块通过质心方法减少了噪声并确保了完整样本处理，避免了传统方法中的裁剪操作，从而提升了检测的准确性和效率。

**关键设计**：在设计中，CAPE模块的参数设置经过精心调整，以优化特征提取效果。同时，CNN的网络结构采用了适合字符级处理的设计，确保了对URL的有效分类。

## 📊 实验亮点

PhishKey在四个最先进的数据集上的实验结果显示，其F1分数高达98.70%，显著优于现有的检测方法。此外，PhishKey对注入攻击等对抗性操作表现出强大的抵抗力，性能下降极小，展示了其在实际应用中的可靠性。

## 🎯 应用场景

PhishKey的研究成果在网络安全领域具有广泛的应用潜力，特别是在防止网络钓鱼攻击的系统中。其高效的检测能力可以帮助企业和个人用户更好地保护敏感信息，降低网络安全风险。未来，该技术还可以扩展到其他类型的网络攻击检测中，提升整体网络安全防护能力。

## 📄 摘要（原文）

> Phishing attacks pose a significant cybersecurity threat, evolving rapidly to bypass detection mechanisms and exploit human vulnerabilities. This paper introduces PhishKey to address the challenges of adaptability, robustness, and efficiency. PhishKey is a novel phishing detection method using automatic feature extraction from hybrid sources. PhishKey combines character-level processing with Convolutional Neural Networks (CNN) for URL classification, and a Centroid-Based Key Component Phishing Extractor (CAPE) for HTML content at the word level. CAPE reduces noise and ensures complete sample processing avoiding crop operations on the input data. The predictions from both modules are integrated using a soft-voting ensemble to achieve more accurate and reliable classifications. Experimental evaluations on four state-of-the-art datasets demonstrate the effectiveness of PhishKey. It achieves up to 98.70% F1 Score and shows strong resistance to adversarial manipulations such as injection attacks with minimal performance degradation.

