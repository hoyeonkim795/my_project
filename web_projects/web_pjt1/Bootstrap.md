# Bootstrap

> Bootstrap은 HTML, CSS, JS로 구성된 오픈소스 라이브러리
>
> 반응형, 모바일 대응을 위한 프론트엔드 컴포넌트

## Utilities

> 아래는 대표적으로 다뤘던 유틸리티 입니다.

* position
* display
* spacing - `margin`, `padding` 
* border
* color
* flex



## Component

* alerts
* badge
* breadcrumb
* button
* card
* carousel
  * JS
* Form / input
* modal
  * JS
* Navbar
  * JS
* Pagination

## grid

> grid system은 균형감 있는 레이아웃을 구성하기 위한 방법이며,
>
> bootstrap에서는 반응형으로 레이아웃 자유롭게 구성할 수 있다.

* [break point](https://getbootstrap.com/docs/4.4/layout/grid/#grid-options)
  * `.col` , `.col-sm`, `.col-md`, `.col-lg`, `.col-xl`

* `.container`
  * 항상 bootstrap의 grid system을 사용하려면, 상위에 `.container`가 존재해야 합니다.
  * `.container`
  * `.container-fluid`
* `.row`
  * 12개의 컬럼으로 구성
  * `.col-{breakpoint}-{number}`



## 미디어쿼리 살펴보기

```css
// Extra small devices (portrait phones, less than 576px)
@media (max-width: 575.98px) { ... }

// Small devices (landscape phones, 576px and up)
@media (min-width: 576px) and (max-width: 767.98px) { ... }

// Medium devices (tablets, 768px and up)
@media (min-width: 768px) and (max-width: 991.98px) { ... }

// Large devices (desktops, 992px and up)
@media (min-width: 992px) and (max-width: 1199.98px) { ... }

// Extra large devices (large desktops, 1200px and up)
@media (min-width: 1200px) { ... }
```

```css
// Extra small devices (portrait phones, less than 576px)
// No media query for `xs` since this is the default in Bootstrap

// Small devices (landscape phones, 576px and up)
@media (min-width: 576px) { ... }

// Medium devices (tablets, 768px and up)
@media (min-width: 768px) { ... }

// Large devices (desktops, 992px and up)
@media (min-width: 992px) { ... }

// Extra large devices (large desktops, 1200px and up)
@media (min-width: 1200px) { ... }
```

