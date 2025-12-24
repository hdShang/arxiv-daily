---
layout: default
title: "Hidden in the Noise: Unveiling Backdoors in Audio LLMs Alignment through Latent Acoustic Pattern Triggers"
---

# Hidden in the Noise: Unveiling Backdoors in Audio LLMs Alignment through Latent Acoustic Pattern Triggers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02175" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02175v3</a>
  <a href="https://arxiv.org/pdf/2508.02175.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02175v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02175v3', 'Hidden in the Noise: Unveiling Backdoors in Audio LLMs Alignment through Latent Acoustic Pattern Triggers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liang Lin, Miao Yu, Kaiwen Luo, Yibo Zhang, Lilan Peng, Dexian Wang, Xuehai Tang, Yuanhe Zhang, Xikang Yang, Zhenhong Zhou, Kun Wang, Yang Liu

**分类**: cs.SD, cs.CL, eess.AS

**发布日期**: 2025-08-04 (更新: 2025-11-18)

---

## 💡 一句话要点

**提出HIN框架以揭示音频大语言模型中的后门攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频大语言模型` `后门攻击` `声学特征` `安全性评估` `深度学习`

## 📋 核心要点

1. 核心问题：现有音频大语言模型在面对声学触发器时存在显著的安全漏洞，亟需深入研究其脆弱性。
2. 方法要点：本文提出HIN框架，通过对音频波形进行声学修改，利用微妙的特征引入后门触发器。
3. 实验或效果：实验表明，音频特征如环境噪声和语速变化的攻击成功率超过90%，显示出ALLMs的显著脆弱性。

## 📝 摘要（中文）

随着音频大语言模型（ALLMs）作为强大的语音处理工具的出现，其安全性问题亟需关注。尽管已有研究探讨了文本和视觉的安全性，但音频的独特特性带来了显著挑战。本文首先研究了ALLM是否容易受到利用声学触发器的后门攻击。为此，我们提出了HIN框架，旨在利用微妙的音频特征。HIN对原始音频波形进行声学修改，引入一致的模式，使ALLM的声学特征编码器能够捕捉到这些触发器。通过开发AudioSafe基准，我们评估了ALLM对音频特征触发器的鲁棒性，实验结果揭示了现有ALLMs的关键脆弱性。

## 🔬 方法详解

**问题定义**：本文旨在解决音频大语言模型（ALLMs）在声学触发器攻击下的脆弱性问题。现有方法对音频特征的安全性研究不足，导致模型容易受到后门攻击。

**核心思路**：论文提出HIN框架，利用音频特有的微妙特征进行后门攻击。通过对音频波形进行声学修改，HIN能够引入一致的触发模式，从而使ALLM的声学特征编码器捕捉到这些模式。

**技术框架**：HIN框架包括多个模块，首先对原始音频进行声学修改，接着通过特征编码器提取音频特征，最后评估模型对这些特征的敏感性。

**关键创新**：HIN框架的创新在于其针对音频特征的后门攻击设计，特别是通过引入时间动态和频谱噪声的变化，显著提高了攻击的隐蔽性和有效性。

**关键设计**：在HIN框架中，关键参数包括声学修改的幅度和频谱噪声的特征设计，损失函数则侧重于最大化触发器的可检测性，同时保持音频的自然性。实验中使用了AudioSafe基准来评估模型的鲁棒性。

## 📊 实验亮点

实验结果显示，利用环境噪声和语速变化等音频特征进行攻击的成功率超过90%。此外，ALLMs对不同声学特征的敏感性差异显著，尤其对音量变化的反应较小，表明攻击的隐蔽性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括音频处理系统的安全性评估、语音识别和合成系统的防护措施等。通过揭示音频大语言模型中的后门攻击，研究为提升模型的安全性和可靠性提供了重要参考，未来可能影响音频技术的广泛应用。

## 📄 摘要（原文）

> As Audio Large Language Models (ALLMs) emerge as powerful tools for speech processing, their safety implications demand urgent attention. While considerable research has explored textual and vision safety, audio's distinct characteristics present significant challenges. This paper first investigates: Is ALLM vulnerable to backdoor attacks exploiting acoustic triggers? In response to this issue, we introduce Hidden in the Noise (HIN), a novel backdoor attack framework designed to exploit subtle, audio-specific features. HIN applies acoustic modifications to raw audio waveforms, such as alterations to temporal dynamics and strategic injection of spectrally tailored noise. These changes introduce consistent patterns that an ALLM's acoustic feature encoder captures, embedding robust triggers within the audio stream. To evaluate ALLM robustness against audio-feature-based triggers, we develop the AudioSafe benchmark, assessing nine distinct risk types. Extensive experiments on AudioSafe and three established safety datasets reveal critical vulnerabilities in existing ALLMs: (I) audio features like environment noise and speech rate variations achieve over 90% average attack success rate. (II) ALLMs exhibit significant sensitivity differences across acoustic features, particularly showing minimal response to volume as a trigger, and (III) poisoned sample inclusion causes only marginal loss curve fluctuations, highlighting the attack's stealth.

