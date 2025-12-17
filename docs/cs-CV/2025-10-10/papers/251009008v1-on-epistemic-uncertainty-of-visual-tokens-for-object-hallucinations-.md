---
layout: default
title: On Epistemic Uncertainty of Visual Tokens for Object Hallucinations in Large Vision-Language Models
---

# On Epistemic Uncertainty of Visual Tokens for Object Hallucinations in Large Vision-Language Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.09008" target="_blank" class="toolbar-btn">arXiv: 2510.09008v1</a>
    <a href="https://arxiv.org/pdf/2510.09008.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09008v1" 
            onclick="toggleFavorite(this, '2510.09008v1', 'On Epistemic Uncertainty of Visual Tokens for Object Hallucinations in Large Vision-Language Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Hoigi Seo, Dong Un Kang, Hyunjin Cho, Joohoon Lee, Se Young Chun

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-10-10

---

## 💡 一句话要点

**针对大视觉语言模型中的对象幻觉，提出基于视觉token认知不确定性的缓解方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `对象幻觉` `认知不确定性` `对抗扰动` `视觉编码器`

## 📋 核心要点

1. LVLM存在对象幻觉问题，即生成图像中不存在对象的描述，影响模型可靠性。
2. 通过识别并屏蔽视觉编码器中具有高认知不确定性的视觉token来缓解对象幻觉。
3. 实验表明，该方法能有效减少对象幻觉，并可与其他方法结合进一步提升性能。

## 📝 摘要（中文）

大型视觉语言模型(LVLMs)集成了视觉编码器(VE)和大型语言模型，在各种任务中取得了显著成功。然而，LVLMs仍然面临着对象幻觉等关键挑战，即生成输入图像中不存在的对象的描述。本文认为，VE中不确定的视觉token是导致对象幻觉的关键因素。统计分析表明，具有高认知不确定性的视觉token与幻觉的发生之间存在正相关关系。此外，理论和实验表明，早期VE层中在小的对抗扰动下表现出较大表征偏差的视觉token具有较高的认知不确定性。基于这些发现，本文提出了一种简单而有效的策略，仅通过修改VE来缓解对象幻觉。该方法包括一个使用对抗扰动的代理方法，用于有效地识别不确定的视觉token，以及一种在VE中间层的自注意力过程中屏蔽这些不确定视觉token的方法，从而抑制它们对视觉编码的影响，进而减轻幻觉。大量实验表明，该方法显著减少了LVLMs中的对象幻觉，并且可以与其他现有技术协同工作。

## 🔬 方法详解

**问题定义**：LVLM在生成图像描述时，会产生图像中不存在的对象的描述，即对象幻觉。现有方法未能有效解决视觉编码器中不确定视觉token导致的幻觉问题。

**核心思路**：论文的核心思路是，通过识别视觉编码器中具有高认知不确定性的视觉token，并在视觉编码过程中屏蔽这些token，从而抑制它们对最终生成结果的影响，进而缓解对象幻觉。这种方法基于一个假设：不确定的视觉token是导致对象幻觉的关键因素。

**技术框架**：该方法主要包含两个阶段：1) 使用对抗扰动识别不确定的视觉token。具体来说，通过对输入图像添加小的对抗扰动，观察视觉编码器中各个token的表征变化。表征变化大的token被认为是具有高认知不确定性的token。2) 在视觉编码器的中间层，通过masking机制屏蔽这些不确定的视觉token，从而降低它们对后续视觉编码的影响。

**关键创新**：该方法的关键创新在于，它将对象幻觉问题与视觉token的认知不确定性联系起来，并提出了一种基于对抗扰动的代理方法来高效地识别这些不确定的token。与以往方法不同，该方法直接针对视觉编码器进行修改，而无需修改语言模型。

**关键设计**：1) 使用对抗扰动来估计视觉token的认知不确定性。具体来说，通过计算原始图像和对抗扰动图像的视觉token表征之间的差异来衡量不确定性。2) 在视觉编码器的中间层应用masking机制。选择中间层是因为早期层可能包含过于底层的特征，而后期层可能已经受到了不确定token的影响。3) 对抗扰动的幅度是一个重要的超参数，需要根据具体任务进行调整。

## 📊 实验亮点

实验结果表明，该方法能够显著减少LVLM中的对象幻觉。具体而言，在多个基准数据集上，该方法在降低幻觉率方面取得了显著提升，并且可以与其他现有技术协同工作，进一步提升性能。实验还验证了对抗扰动作为认知不确定性代理的有效性。

## 🎯 应用场景

该研究成果可应用于提升视觉语言模型的可靠性和可信度，尤其是在需要精确图像理解和描述的场景中，例如医疗影像诊断、自动驾驶、智能监控等。通过减少对象幻觉，可以提高模型在这些关键应用中的实用价值。

## 📄 摘要（原文）

> Large vision-language models (LVLMs), which integrate a vision encoder (VE) with a large language model, have achieved remarkable success across various tasks. However, there are still crucial challenges in LVLMs such as object hallucination, generating descriptions of objects that are not in the input image. Here, we argue that uncertain visual tokens within the VE is a key factor that contributes to object hallucination. Our statistical analysis found that there are positive correlations between visual tokens with high epistemic uncertainty and the occurrence of hallucinations. Furthermore, we show theoretically and empirically that visual tokens in early VE layers that exhibit large representation deviations under small adversarial perturbations indicate high epistemic uncertainty. Based on these findings, we propose a simple yet effective strategy to mitigate object hallucination by modifying the VE only. Our method comprises a proxy method with adversarial perturbations for identifying uncertain visual tokens efficiently and a method to mask these uncertain visual tokens during the self-attention process in the middle layers of the VE, suppressing their influence on visual encoding and thus alleviating hallucinations. Extensive experiments show that our method significantly reduces object hallucinations in LVLMs and can synergistically work with other prior arts.

