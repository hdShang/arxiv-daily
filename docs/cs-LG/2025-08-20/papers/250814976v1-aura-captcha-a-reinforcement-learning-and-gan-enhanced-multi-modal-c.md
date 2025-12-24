---
layout: default
title: "Aura-CAPTCHA: A Reinforcement Learning and GAN-Enhanced Multi-Modal CAPTCHA System"
---

# Aura-CAPTCHA: A Reinforcement Learning and GAN-Enhanced Multi-Modal CAPTCHA System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14976" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14976v1</a>
  <a href="https://arxiv.org/pdf/2508.14976.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14976v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14976v1', 'Aura-CAPTCHA: A Reinforcement Learning and GAN-Enhanced Multi-Modal CAPTCHA System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joydeep Chandra, Prabal Manhas, Ramanjot Kaur, Rashi Sahay

**分类**: cs.LG

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出Aura-CAPTCHA以解决传统验证码易被攻破的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态验证码` `生成对抗网络` `强化学习` `大型语言模型` `网络安全` `自动化攻击防护`

## 📋 核心要点

1. 现有验证码方法易被AI技术（如OCR）攻破，安全性不足。
2. Aura-CAPTCHA结合GAN、RL和LLM，生成动态挑战并自适应调整难度。
3. 实验结果显示，系统实现92%的人类成功率和10%的机器人绕过率，表现优异。

## 📝 摘要（中文）

Aura-CAPTCHA是一种多模态验证码系统，旨在解决传统验证码方法在面对AI技术（如光学字符识别和对抗性图像处理）时的脆弱性。该系统结合了生成对抗网络（GAN）生成动态图像挑战，利用强化学习（RL）进行自适应难度调整，并使用大型语言模型（LLM）创建文本和音频提示。视觉挑战包括3x3网格选择，音频挑战则将随机数字和单词结合为一个任务。通过对真实流量的评估，Aura-CAPTCHA实现了92%的人工成功率和10%的机器人绕过率，显著优于现有验证码系统，提供了一种稳健且可扩展的在线应用安全解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决传统验证码在AI技术（如光学字符识别和对抗性图像处理）面前的脆弱性，现有方法难以有效防止自动化攻击。

**核心思路**：Aura-CAPTCHA通过结合生成对抗网络（GAN）和强化学习（RL），生成动态且适应性强的验证码挑战，以提高安全性和用户体验。

**技术框架**：系统主要包括三个模块：生成对抗网络用于生成视觉挑战，强化学习用于根据用户行为调整难度，以及大型语言模型用于生成文本和音频提示。

**关键创新**：该系统的创新在于将GAN与RL结合，动态生成验证码并根据用户反馈实时调整难度，显著提高了防护能力。

**关键设计**：在设计中，视觉挑战采用3x3网格选择，要求用户选择至少三个正确图像；音频挑战则将随机数字和单词结合，增加了挑战的复杂性。

## 📊 实验亮点

实验结果表明，Aura-CAPTCHA在真实流量下实现了92%的人工成功率和仅10%的机器人绕过率，显著优于现有的验证码系统，展示了其在安全性和用户友好性方面的优势。

## 🎯 应用场景

Aura-CAPTCHA可广泛应用于在线安全领域，如电子商务、社交媒体和在线银行等，能够有效防止自动化攻击，提升用户体验。其动态生成和自适应调整的特性使其在未来的网络安全防护中具有重要价值。

## 📄 摘要（原文）

> Aura-CAPTCHA was developed as a multi-modal CAPTCHA system to address vulnerabilities in traditional methods that are increasingly bypassed by AI technologies, such as Optical Character Recognition (OCR) and adversarial image processing. The design integrated Generative Adversarial Networks (GANs) for generating dynamic image challenges, Reinforcement Learning (RL) for adaptive difficulty tuning, and Large Language Models (LLMs) for creating text and audio prompts. Visual challenges included 3x3 grid selections with at least three correct images, while audio challenges combined randomized numbers and words into a single task. RL adjusted difficulty based on incorrect attempts, response time, and suspicious user behavior. Evaluations on real-world traffic demonstrated a 92% human success rate and a 10% bot bypass rate, significantly outperforming existing CAPTCHA systems. The system provided a robust and scalable approach for securing online applications while remaining accessible to users, addressing gaps highlighted in previous research.

