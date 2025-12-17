---
layout: default
title: On Epistemic Uncertainty of Visual Tokens for Object Hallucinations in Large Vision-Language Models
---

# On Epistemic Uncertainty of Visual Tokens for Object Hallucinations in Large Vision-Language Models

**arXiv**: [2510.09008v1](https://arxiv.org/abs/2510.09008) | [PDF](https://arxiv.org/pdf/2510.09008.pdf)

**作者**: Hoigi Seo, Dong Un Kang, Hyunjin Cho, Joohoon Lee, Se Young Chun

---

## 💡 一句话要点

**提出视觉编码器修改策略以缓解大视觉语言模型中的物体幻觉问题**

**关键词**: `大视觉语言模型` `物体幻觉` `视觉编码器` `对抗扰动` `自注意力掩码` `不确定性估计`

## 📋 核心要点

1. 核心问题：大视觉语言模型存在物体幻觉，即生成图像中不存在的物体描述。
2. 方法要点：通过对抗扰动识别不确定视觉令牌，并在自注意力过程中掩码它们。
3. 实验或效果：实验显示该方法显著减少物体幻觉，并能与其他方法协同工作。

## 📄 摘要（原文）

> Large vision-language models (LVLMs), which integrate a vision encoder (VE)
> with a large language model, have achieved remarkable success across various
> tasks. However, there are still crucial challenges in LVLMs such as object
> hallucination, generating descriptions of objects that are not in the input
> image. Here, we argue that uncertain visual tokens within the VE is a key
> factor that contributes to object hallucination. Our statistical analysis found
> that there are positive correlations between visual tokens with high epistemic
> uncertainty and the occurrence of hallucinations. Furthermore, we show
> theoretically and empirically that visual tokens in early VE layers that
> exhibit large representation deviations under small adversarial perturbations
> indicate high epistemic uncertainty. Based on these findings, we propose a
> simple yet effective strategy to mitigate object hallucination by modifying the
> VE only. Our method comprises a proxy method with adversarial perturbations for
> identifying uncertain visual tokens efficiently and a method to mask these
> uncertain visual tokens during the self-attention process in the middle layers
> of the VE, suppressing their influence on visual encoding and thus alleviating
> hallucinations. Extensive experiments show that our method significantly
> reduces object hallucinations in LVLMs and can synergistically work with other
> prior arts.

